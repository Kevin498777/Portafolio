"""
Management command: python manage.py load_habilidades

Carga las habilidades del CV en la base de datos.
Si ya existe (por nombre), la actualiza.
Edita los niveles desde /admin/ después de correr este comando.
"""
from django.core.management.base import BaseCommand
from core.models import Habilidad


HABILIDADES = [
    # --- Lenguajes ---
    {"nombre": "Python",      "categoria": "lenguaje", "nivel": 80, "orden": 1},
    {"nombre": "JavaScript",  "categoria": "lenguaje", "nivel": 60, "orden": 2},
    {"nombre": "SQL",         "categoria": "lenguaje", "nivel": 50, "orden": 3},
    {"nombre": "HTML5",       "categoria": "lenguaje", "nivel": 40, "orden": 4},
    {"nombre": "CSS3",        "categoria": "lenguaje", "nivel": 40, "orden": 5},
    {"nombre": "Java",        "categoria": "lenguaje", "nivel": 30, "orden": 8},

    # --- Frameworks ---
    {"nombre": "Django",      "categoria": "framework", "nivel": 80, "orden": 1},
    {"nombre": "Flask",       "categoria": "framework", "nivel": 80, "orden": 2},
    {"nombre": "FastAPI",     "categoria": "framework", "nivel": 70, "orden": 3},
    {"nombre": "PyQt5",       "categoria": "framework", "nivel": 50, "orden": 4},
    {"nombre": "Tkinter",     "categoria": "framework", "nivel": 70, "orden": 5},

    # --- Bases de Datos ---
    {"nombre": "PostgreSQL",  "categoria": "bd", "nivel": 80, "orden": 1},
    {"nombre": "MySQL",       "categoria": "bd", "nivel": 60, "orden": 2},
    {"nombre": "SQLite",      "categoria": "bd", "nivel": 70, "orden": 3},
    {"nombre": "MongoDB",     "categoria": "bd", "nivel": 80, "orden": 4},

    # --- Automatización ---
    {"nombre": "Selenium WebDriver", "categoria": "automatizacion", "nivel": 65, "orden": 1},

    # --- Herramientas ---
    {"nombre": "Git y GitHub",       "categoria": "herramienta", "nivel": 70, "orden": 1},
    {"nombre": "Pandas",             "categoria": "herramienta", "nivel": 35, "orden": 2},
    {"nombre": "OpenPyXL",           "categoria": "herramienta", "nivel": 40, "orden": 3},
    {"nombre": "Visual Studio Code", "categoria": "herramienta", "nivel": 80, "orden": 4},
    {"nombre": "PyInstaller",        "categoria": "herramienta", "nivel": 70, "orden": 5},
    {"nombre": "Inno Setup",         "categoria": "herramienta", "nivel": 50, "orden": 6},
]


class Command(BaseCommand):
    help = "Carga las habilidades del CV en la base de datos."

    def handle(self, *args, **options):
        creadas = 0
        actualizadas = 0

        for datos in HABILIDADES:
            _, created = Habilidad.objects.update_or_create(
                nombre=datos["nombre"],
                defaults=datos,
            )
            if created:
                creadas += 1
                self.stdout.write(self.style.SUCCESS(f"✓ {datos['categoria']:15} {datos['nombre']}"))
            else:
                actualizadas += 1
                self.stdout.write(f"↺ {datos['categoria']:15} {datos['nombre']}")

        self.stdout.write(
            self.style.SUCCESS(
                f"\nListo: {creadas} creadas, {actualizadas} actualizadas."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                "\nRecuerda ajustar los niveles desde /admin/ → Habilidades."
            )
        )
