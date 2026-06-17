# Tutorial: Desplegar el Portafolio en Railway (con PostgreSQL persistente)

Railway es una alternativa a Render. La diferencia clave en esta configuración:
vamos a usar una base de datos **PostgreSQL real** (no SQLite), así que tus
proyectos, habilidades y los cambios que hagas desde `/admin/` en producción
**no se borran** en cada deploy.

Ya preparé el proyecto para esto:
- `settings.py` ahora detecta automáticamente si existe una variable
  `DATABASE_URL` (la usa) o si no, usa SQLite local para tu computadora.
- Se agregó `dj-database-url` a `requirements.txt`.
- El `Procfile` ya incluye `collectstatic`, `migrate` y los comandos de
  carga de proyectos/habilidades antes de iniciar el servidor.

## 0. Sube tus cambios a GitHub

```
git add -A
git commit -m "Soporte para PostgreSQL en Railway"
git push origin kevin
```

## 1. Crear cuenta en Railway

1. Ve a https://railway.app
2. Inicia sesión con tu cuenta de GitHub (más simple, ya queda conectado).

## 2. Crear el proyecto

1. En el dashboard, clic en **New Project**.
2. Selecciona **Deploy from GitHub repo**.
3. Elige `Kevin498777/Portafolio` y la rama `kevin`.
4. Railway detecta que es un proyecto Python y empieza a construirlo
   automáticamente (usa tu `Procfile` para saber cómo arrancarlo).

## 3. Agregar la base de datos PostgreSQL

1. Dentro de tu proyecto en Railway, clic en **New** → **Database** →
   **Add PostgreSQL**.
2. Railway crea la base de datos y, automáticamente, agrega la variable de
   entorno `DATABASE_URL` a tu servicio web (no tienes que copiarla a mano,
   Railway conecta ambos servicios solo).

## 4. Configurar variables de entorno del servicio web

Entra a tu servicio web (no el de la base de datos) → pestaña **Variables** →
agrega:

| Variable | Valor |
|---|---|
| `SECRET_KEY` | una cadena larga y aleatoria (puedes generar una en https://djecrety.ir) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.up.railway.app` |

`DATABASE_URL` ya la agregó Railway automáticamente al conectar el Postgres
del paso 3 — no la toques.

## 5. Generar el dominio público

1. En tu servicio web → pestaña **Settings** → sección **Networking**.
2. Clic en **Generate Domain**. Railway te da una URL como
   `kevin-portfolio.up.railway.app`.

## 6. Esperar el deploy

Ve a la pestaña **Deployments** → abre el deploy en curso → pestaña **Logs**.
Vas a ver, en orden:

```
Collecting static files...
Applying migrations...
Creado: ... (cada proyecto)
Creada: ... (cada habilidad)
[gunicorn arrancando]
```

Cuando veas que gunicorn quedó escuchando, abre la URL generada en el paso 5.

## 7. Crear tu superusuario (solo la primera vez)

Como ahora usas PostgreSQL persistente, solo necesitas hacer esto **una vez**
(a diferencia de SQLite efímero, no se vuelve a borrar en cada deploy):

1. Instala el CLI de Railway si no lo tienes: `npm i -g @railway/cli`
   (o revisa la documentación de Railway si prefieres otro método de
   instalación).
2. En tu terminal, dentro de la carpeta del proyecto:
   ```
   railway login
   railway link
   railway run python manage.py createsuperuser
   ```
3. Sigue las instrucciones para crear tu usuario y contraseña de admin.

Alternativa sin CLI: en el dashboard de Railway, abre tu servicio web →
pestaña **Settings** → busca la opción de abrir una terminal/shell remota si
tu plan la incluye, y corre el mismo comando ahí.

## 8. Verificar que todo funciona

1. Abre tu URL de Railway.
2. Revisa Inicio, Proyectos y Contacto.
3. Entra a `/admin/` con el superusuario que acabas de crear.
4. Prueba editar el nivel de una habilidad desde el admin, recarga la página
   de Habilidades y confirma que el cambio se vea — y que **siga ahí** después
   de hacer otro `git push` (a diferencia de Render con SQLite, aquí sí
   persiste).

## 9. Futuros cambios

```
git add -A
git commit -m "mensaje describiendo el cambio"
git push origin kevin
```

Railway detecta el push y vuelve a desplegar automáticamente. Como la base de
datos es persistente, tus proyectos solo se actualizan (no se duplican ni se
borran), y tus mensajes de contacto y cambios de admin se mantienen.

## Nota sobre las imágenes de proyectos (`media/`)

Las imágenes que subiste a `media/proyectos/` ya están en tu repositorio de
Git (ya quitamos `media/` del `.gitignore`), así que se despliegan junto con
el código. Si en el futuro subes una imagen nueva **desde el panel admin en
producción** (no desde tu computadora), esa imagen se guardará en el disco
del contenedor de Railway, que también es efímero — se perdería en el
siguiente deploy. Si planeas subir imágenes nuevas seguido desde producción,
avísame y configuramos un volumen persistente de Railway o almacenamiento en
la nube (Cloudinary, como ya usas en tu proyecto nixi-farmacia).
