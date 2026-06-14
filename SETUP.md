# Setup inicial del portafolio

## 1. Instalar dependencias (en tu terminal, dentro de la carpeta)

```bash
cd "C:\Users\El 498\Desktop\GitHub\Portafolio"
pip install -r requirements.txt
```

## 2. Configurar variables de entorno

Copia `.env.example` a `.env`:
```bash
copy .env.example .env
```
Luego edita `.env` y cambia `SECRET_KEY` por cualquier cadena larga aleatoria.

## 3. Crear la base de datos

```bash
python manage.py migrate
python manage.py createsuperuser
```

## 4. Correr localmente

```bash
python manage.py runserver
```
Abre http://127.0.0.1:8000 en tu navegador.
Panel admin: http://127.0.0.1:8000/admin

## 5. Agregar tus datos

Entra al admin y agrega:
- **Habilidades**: Python (90%), Django (85%), PostgreSQL (80%), etc.
- **Proyectos**: Automatización AMPM, Se'si Eskani (marcar como "destacado")

## 6. Git — primer commit

```bash
git add .
git commit -m "feat: initial portfolio project"
```

## 7. Conectar con GitHub

1. Ve a https://github.com/new
2. Crea un repositorio llamado `portafolio` (sin README, vacío)
3. Copia la URL HTTPS que te da GitHub, por ejemplo:
   `https://github.com/TU_USUARIO/portafolio.git`
4. En tu terminal:

```bash
git remote add origin https://github.com/TU_USUARIO/portafolio.git
git branch -M main
git push -u origin main
```

## 8. Deploy en Render (gratis)

1. Ve a https://render.com y crea cuenta con GitHub
2. "New Web Service" → elige tu repositorio `portafolio`
3. Render detecta automáticamente el `render.yaml`
4. Agrega variable de entorno `SECRET_KEY` con una clave segura
5. Click "Deploy" — en ~3 minutos tienes tu URL pública

---
**Stack**: Django 5 · Python · Bootstrap 5 · WhiteNoise · Render
