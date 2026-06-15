"""
Management command: python manage.py load_proyectos

Carga todos los proyectos del portafolio en la base de datos.
Si el proyecto ya existe (por título), lo actualiza.
"""
from django.core.management.base import BaseCommand
from django.core.files import File
from core.models import Proyecto
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
))))
MEDIA_PROYECTOS = os.path.join(BASE_DIR, "media", "proyectos")


PROYECTOS = [
    {
        "titulo": "AMPMAuto — Automatización de Registro de Guías",
        "descripcion": (
            "Aplicación de escritorio que automatiza el registro masivo de guías en el "
            "portal AMPM mediante Selenium, reduciendo horas de trabajo manual a minutos "
            "con una velocidad de 10–15 guías por minuto."
        ),
        "descripcion_larga": (
            "AMPMAuto es una aplicación de escritorio desarrollada con Python, Selenium y PyQt5 "
            "para automatizar el registro masivo de guías en el portal AMPM. El sistema surgió de "
            "la necesidad de reducir el tiempo y los errores del proceso manual de captura. "
            "Permite cargar múltiples guías, realizar el registro automático y validar el estado "
            "de cada una en tiempo real. Incorpora detección inteligente de guías previamente "
            "entregadas o con inconsistencias, evitando duplicidades. Genera reportes automáticos "
            "en Excel con el resultado de cada operación. Empaquetado como instalador .exe con "
            "PyInstaller e Inno Setup para distribución en Windows."
        ),
        "tecnologias": "Python, Selenium WebDriver, PyQt5, OpenPyXL, Pandas, PyInstaller, Inno Setup",
        "url_github": "https://github.com/Kevin498777/AMPMAuto",
        "url_demo": "",
        "imagen_archivo": "ampm_auto_1.png",
        "destacado": True,
        "orden": 1,
    },
    {
        "titulo": "Se'si Eskani — Monitoreo de Atributos de Egreso",
        "descripcion": (
            "Plataforma web para centralizar el monitoreo de atributos de egreso requeridos "
            "por la acreditación CACEI, sustituyendo hojas de cálculo con una solución "
            "escalable y con reportes automáticos."
        ),
        "descripcion_larga": (
            "Se'si Eskani es una plataforma web desarrollada como proyecto integrador para el "
            "Instituto Tecnológico Superior de Huetamo. Fue diseñada para sustituir la gestión "
            "manual basada en hojas de cálculo, proporcionando una solución centralizada para "
            "el seguimiento y evaluación de atributos de egreso en procesos de acreditación CACEI. "
            "Permite registrar evidencias, monitorear el cumplimiento de indicadores y generar "
            "reportes automáticos para apoyar la toma de decisiones. Incluye herramientas de "
            "visualización del avance de cada atributo, reduciendo la carga administrativa y "
            "mejorando la organización de la información para docentes y personal administrativo."
        ),
        "tecnologias": "Django, HTML, SASS, PostgreSQL, Docker, Nginx, Node.js",
        "url_github": "https://github.com/Pato1YT/PlataformaCACEI",
        "url_demo": "",
        "imagen_archivo": None,
        "destacado": True,
        "orden": 2,
    },
    {
        "titulo": "nixi-farmacia — Plataforma Digital de Farmacia",
        "descripcion": (
            "Aplicación web full-stack con roles para pacientes, farmacéuticos y médicos. "
            "Incluye carrito de compras, recetas digitales, chatbot con OpenAI y gestión "
            "de inventario con imágenes en Cloudinary."
        ),
        "descripcion_larga": (
            "Nixi Farmacia Digital es una aplicación web full-stack que digitaliza la operación "
            "de una farmacia. Implementa autenticación con JWT y tres roles: paciente, farmacéutico "
            "y médico. Los pacientes pueden explorar el catálogo, gestionar un carrito de compras "
            "persistente, crear pedidos, subir recetas y consultar historial de pagos. Los "
            "farmacéuticos administran el inventario con soporte de imágenes en Cloudinary. Los "
            "médicos gestionan citas y emiten recetas digitales. Incluye un chatbot integrado con "
            "la API de OpenAI, generación de reportes y alertas de interacciones entre medicamentos. "
            "Backend desplegado en Railway con PostgreSQL y frontend con Vite."
        ),
        "tecnologias": "Django 5, Django REST Framework, SimpleJWT, PostgreSQL, React, Vite, Tailwind CSS, Cloudinary, OpenAI API, Docker",
        "url_github": "https://github.com/Kevin498777/nixi-farmacia",
        "url_demo": "",
        "imagen_archivo": None,
        "destacado": True,
        "orden": 3,
    },
    {
        "titulo": "Habit Tracker — Seguimiento de Hábitos Personales",
        "descripcion": (
            "Aplicación web para registrar, monitorear y mantener hábitos diarios con "
            "estadísticas personalizadas, autenticación Firebase y sincronización en la nube."
        ),
        "descripcion_larga": (
            "Habit Tracker es una aplicación web diseñada para facilitar la creación y seguimiento "
            "de hábitos personales. Permite registrar actividades recurrentes, marcar su cumplimiento "
            "diario y visualizar el progreso mediante métricas e indicadores visuales. Incorpora "
            "autenticación de usuarios con Firebase Authentication, almacenamiento en Cloud Firestore "
            "y sincronización en la nube para acceder desde cualquier dispositivo. Desarrollada con "
            "Angular y TypeScript aplicando buenas prácticas de diseño de interfaces."
        ),
        "tecnologias": "Angular, TypeScript, Firebase Authentication, Cloud Firestore, HTML5, CSS3",
        "url_github": "https://github.com/Kevin498777/Habit_Tracker",
        "url_demo": "https://habit-tracker-498.web.app/login",
        "imagen_archivo": None,
        "destacado": False,
        "orden": 4,
    },
    {
        "titulo": "KneeMotion — Sistema de Rehabilitación de Rodilla",
        "descripcion": (
            "Plataforma clínica web para monitoreo de rehabilitación de rodilla: gestiona "
            "pacientes, dispositivos de medición y sesiones de terapia con métricas biomecánicas "
            "en tiempo real (ángulo, fuerza, temperatura, estimulación FES)."
        ),
        "descripcion_larga": (
            "KneeMotion es un sistema clínico desarrollado con Laravel 12 y Filament 3 para el "
            "seguimiento de pacientes en rehabilitación de rodilla. Presentado en el Inovatec local "
            "del Instituto Tecnológico de Huetamo. Registra sesiones de terapia con métricas "
            "biomecánicas (ángulo de movimiento, fuerza, temperatura, intensidad FES — Functional "
            "Electrical Stimulation), gestiona dispositivos físicos de medición con control de "
            "firmware y sincronización, y permite a los terapeutas llevar historial clínico completo "
            "por paciente. El panel con Filament ofrece dashboards interactivos y gestión de datos médicos."
        ),
        "tecnologias": "PHP, Laravel 12, Filament 3, Livewire 3, MySQL, Vite, Blade",
        "url_github": "https://github.com/Pato1YT/KneeMotion",
        "url_demo": "",
        "imagen_archivo": None,
        "destacado": False,
        "orden": 5,
    },
    {
        "titulo": "Lucky Game — RPG de Aventura 2D",
        "descripcion": (
            "Videojuego RPG 2D desarrollado en Python con Pygame, con sistema de combate "
            "por turnos, tienda, ruleta tipo gacha y exploración de mapas por tiles."
        ),
        "descripcion_larga": (
            "Lucky Game (Elementary Lucky) es un videojuego RPG desarrollado desde cero en Python "
            "con arquitectura modular orientada a objetos. Incluye pantalla de login, menú principal, "
            "exploración de mundo con mapas por tiles usando PyTMX, sistema de combate por turnos, "
            "tienda de ítems, ruleta tipo gacha para obtener personajes con habilidades únicas y "
            "pantalla de Game Over. Corre en pantalla completa con delta time para animaciones "
            "fluidas independientes del hardware. Gestor de pantallas centralizado (GestorPantallas) "
            "y estado global del juego (GameState)."
        ),
        "tecnologias": "Python, Pygame-CE, PyTMX, Pillow",
        "url_github": "https://github.com/Kevin498777/Lucky_Game",
        "url_demo": "",
        "imagen_archivo": "lucky_game.png",
        "destacado": False,
        "orden": 6,
    },
    {
        "titulo": "DeliPostres — E-commerce de Postres Artesanales",
        "descripcion": (
            "Landing page con catálogo de productos, carrusel de imágenes y formulario de "
            "pedidos para una pastelería artesanal a domicilio. Diseño responsive desplegado en Vercel."
        ),
        "descripcion_larga": (
            "Plataforma web tipo e-commerce para DeliPostres, una pastelería artesanal a domicilio. "
            "Incluye catálogo de 6 productos con precios, carrusel de imágenes animado, sección de "
            "categorías, opiniones de clientes y formulario de pedidos personalizado. Diseño completamente "
            "responsive adaptado a dispositivos móviles y escritorio. Desplegado en Vercel. "
            "Proyecto desarrollado en equipo."
        ),
        "tecnologias": "HTML5, CSS3, JavaScript, Vercel",
        "url_github": "",
        "url_demo": "https://e-commerce-postres.vercel.app/",
        "imagen_archivo": None,
        "destacado": False,
        "orden": 7,
    },
    {
        "titulo": "Recetapp — Recetario Personal con Lista de Compras",
        "descripcion": (
            "App móvil multiplataforma para gestionar recetas personales con generación "
            "automática de lista de compras. Disponible para Android, iOS y escritorio."
        ),
        "descripcion_larga": (
            "Recetapp es una aplicación desarrollada con Flutter que funciona como recetario "
            "personal digital multiplataforma. Permite crear, guardar y consultar recetas, y genera "
            "automáticamente una lista de compras basada en los ingredientes de cada receta. Usa SQLite "
            "como base de datos local con autenticación mediante hash criptográfico para protección de "
            "datos. Disponible para Android, iOS y escritorio. Publicada como APK en GitHub Releases."
        ),
        "tecnologias": "Flutter, Dart, SQLite, shared_preferences, Material Design",
        "url_github": "https://github.com/AnaSanchez21/recetapp",
        "url_demo": "",
        "imagen_archivo": "recetapp.png",
        "destacado": False,
        "orden": 8,
    },
]


class Command(BaseCommand):
    help = "Carga todos los proyectos del portafolio en la base de datos."

    def handle(self, *args, **options):
        creados = 0
        actualizados = 0

        for datos in PROYECTOS:
            imagen_archivo = datos.pop("imagen_archivo")

            proyecto, created = Proyecto.objects.update_or_create(
                titulo=datos["titulo"],
                defaults={k: v for k, v in datos.items()},
            )

            # Asignar imagen si existe y no tiene una ya
            if imagen_archivo and not proyecto.imagen:
                ruta = os.path.join(MEDIA_PROYECTOS, imagen_archivo)
                if os.path.exists(ruta):
                    with open(ruta, "rb") as f:
                        proyecto.imagen.save(imagen_archivo, File(f), save=True)
                    self.stdout.write(f"  Imagen asignada: {imagen_archivo}")
                else:
                    self.stdout.write(
                        self.style.WARNING(f"  Imagen no encontrada: {ruta}")
                    )

            if created:
                creados += 1
                self.stdout.write(self.style.SUCCESS(f"✓ Creado: {proyecto.titulo}"))
            else:
                actualizados += 1
                self.stdout.write(f"↺ Actualizado: {proyecto.titulo}")

        self.stdout.write(
            self.style.SUCCESS(
                f"\nListo: {creados} creados, {actualizados} actualizados."
            )
        )
