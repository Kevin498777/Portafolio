# Tutorial: Desplegar el Portafolio en Render

Tu proyecto ya tiene el archivo `render.yaml` configurado, así que Render puede
leer toda la configuración automáticamente (esto se llama "Blueprint"). Solo
necesitas seguir estos pasos.

## 0. Antes de empezar: sube tus cambios a GitHub

Render despliega directamente desde tu repositorio de GitHub, así que primero
necesita ver tus últimos cambios ahí. En tu terminal, dentro de la carpeta del
proyecto:

```
git add -A
git commit -m "Fix de proyectos duplicados, habilidades reales, despliegue"
git push origin kevin
```

Verifica en https://github.com/Kevin498777/Portafolio/tree/kevin que tus
archivos más recientes ya aparecen ahí.

## 1. Crear cuenta en Render

1. Ve a https://render.com
2. Crea una cuenta (puedes usar "Sign up with GitHub" para conectar tu cuenta
   directamente, es lo más simple).
3. Autoriza a Render a acceder a tus repositorios de GitHub cuando te lo pida.

## 2. Crear el servicio desde el Blueprint

1. En el Dashboard de Render, haz clic en **New +** (arriba a la derecha) →
   **Blueprint**.
2. Busca y selecciona tu repositorio `Kevin498777/Portafolio`.
3. Render detectará automáticamente el archivo `render.yaml` y te mostrará el
   servicio `kevin-portfolio` listo para crear.
4. Asegúrate de que la rama (**Branch**) seleccionada sea `kevin` (es la única
   que tienes, así que debería aparecer por defecto).
5. Haz clic en **Apply** / **Create New Resources**.

## 3. Variables de entorno

El `render.yaml` ya define estas automáticamente, no necesitas tocarlas:

- `DEBUG` = `False`
- `SECRET_KEY` = Render genera una clave segura automáticamente
- `ALLOWED_HOSTS` = `.onrender.com`

Si en algún momento quieres revisarlas o cambiarlas: entra al servicio →
pestaña **Environment**.

## 4. Esperar el primer build

Render va a ejecutar automáticamente (definido en `render.yaml`):

```
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py load_proyectos
python manage.py load_habilidades
```

Esto tarda entre 2 y 5 minutos la primera vez. Puedes ver el progreso en vivo
en la pestaña **Logs** del servicio. Busca la línea final que diga algo como
`Your service is live`.

## 5. Verificar que todo funciona

1. Abre la URL que te da Render (algo como
   `https://kevin-portfolio.onrender.com`).
2. Revisa que las secciones Inicio, Proyectos y Contacto carguen bien.
3. Entra a `/admin/` con tu usuario y contraseña habituales para confirmar el
   acceso (el `auth_user` no se crea en cada deploy, pero como acabamos de
   reconstruir tu base de datos local con tu usuario y contraseña reales, el
   primer deploy en Render creará un usuario **vacío** — ver advertencia abajo).

## ⚠️ Importante: tu base de datos en Render es temporal

Tu proyecto usa SQLite sin disco persistente. Esto significa:

- **Cada vez que hagas un nuevo deploy** (cada `git push`), Render crea una
  base de datos nueva desde cero y vuelve a correr `load_proyectos` y
  `load_habilidades`. Tus proyectos y habilidades siempre se recrean igual,
  así que no hay riesgo ahí.
- **Pero tu usuario admin no se crea automáticamente.** Como no hay comando
  que cree tu superusuario en el `buildCommand`, después de cada deploy
  necesitas crear tu usuario admin manualmente la primera vez (o agregar un
  paso al build, ver opción abajo).
- **Cualquier mensaje de contacto recibido, o cambios que hagas a mano desde
  el panel admin en producción** (por ejemplo ajustar manualmente un nivel de
  habilidad ahí) **se perderán en el siguiente deploy**, porque la base de
  datos completa se recrea desde cero.

### Cómo crear tu superusuario en Render (primera vez)

1. En el dashboard del servicio, abre la pestaña **Shell** (Render te da una
   terminal conectada a tu app en vivo).
2. Corre:
   ```
   python manage.py createsuperuser
   ```
3. Sigue las instrucciones para crear tu usuario y contraseña.

Tendrás que repetir esto cada vez que Render reconstruya la base de datos
desde cero (por ejemplo, si el servicio se reinicia tras estar inactivo, o en
cada nuevo deploy). Si quieres evitar este paso manual cada vez, dime y te
ayudo a automatizarlo con un script que cree el superusuario solo si no
existe ya, usando variables de entorno para el usuario/contraseña.

## 6. Futuros cambios

Cada vez que quieras actualizar el sitio en vivo, solo necesitas:

```
git add -A
git commit -m "mensaje describiendo el cambio"
git push origin kevin
```

Render detecta el push automáticamente y vuelve a desplegar.
