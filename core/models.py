from django.db import models


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    descripcion_larga = models.TextField(blank=True)
    tecnologias = models.CharField(max_length=300)
    url_github = models.URLField(blank=True)
    url_demo = models.URLField(blank=True)
    imagen = models.ImageField(upload_to="proyectos/", blank=True, null=True)
    destacado = models.BooleanField(default=False)
    orden = models.PositiveSmallIntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["orden", "-fecha"]

    def __str__(self):
        return self.titulo

    def get_tecnologias_list(self):
        return [t.strip() for t in self.tecnologias.split(",")]


class Habilidad(models.Model):
    CATEGORIAS = [
        ("lenguaje", "Lenguajes"),
        ("framework", "Frameworks"),
        ("bd", "Bases de Datos"),
        ("herramienta", "Herramientas"),
        ("automatizacion", "Automatizacion"),
    ]
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    nivel = models.PositiveSmallIntegerField(default=80)
    orden = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["categoria", "orden"]

    def __str__(self):
        return self.nombre


class Mensaje(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"
