"""
Management command: python manage.py dedupe_proyectos

Elimina filas duplicadas de Proyecto que comparten el mismo título,
conservando solo la más reciente (por id mas alto) de cada grupo.
Útil si por error se generaron proyectos duplicados (por ejemplo,
al correr load_proyectos varias veces con datos inconsistentes).
"""
from django.core.management.base import BaseCommand
from django.db.models import Count
from core.models import Proyecto


class Command(BaseCommand):
    help = "Elimina proyectos duplicados (mismo título), dejando solo uno por título."

    def handle(self, *args, **options):
        duplicados = (
            Proyecto.objects.values("titulo")
            .annotate(total=Count("id"))
            .filter(total__gt=1)
        )

        if not duplicados:
            self.stdout.write(self.style.SUCCESS("No se encontraron proyectos duplicados."))
            return

        total_borrados = 0
        for grupo in duplicados:
            titulo = grupo["titulo"]
            filas = list(Proyecto.objects.filter(titulo=titulo).order_by("id"))
            # Conserva la última (id más alto), borra el resto
            a_borrar = filas[:-1]
            for p in a_borrar:
                self.stdout.write(f"  Borrando duplicado id={p.id}: {p.titulo}")
                p.delete()
                total_borrados += 1

        self.stdout.write(
            self.style.SUCCESS(f"\nListo: {total_borrados} duplicados eliminados.")
        )
