from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]

# Django's static() helper solo sirve /media/ cuando DEBUG=True. Para un
# sitio pequeño como este, en producción (Render, DEBUG=False) también
# servimos /media/ directamente con esta vista. Si el tráfico crece mucho
# en el futuro, conviene mover las imágenes a un servicio externo como
# Cloudinary o S3 en vez de servirlas desde Django.
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]
