from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Proyecto, Habilidad, Mensaje
from .forms import ContactoForm


def home(request):
    proyectos_destacados = Proyecto.objects.filter(destacado=True)[:3]
    habilidades = Habilidad.objects.all()

    habilidades_por_categoria_raw = {}
    for h in habilidades:
        cat = h.get_categoria_display()
        habilidades_por_categoria_raw.setdefault(cat, []).append(h)

    # Ordenar categorías: más habilidades primero
    habilidades_por_categoria = dict(
        sorted(habilidades_por_categoria_raw.items(), key=lambda x: len(x[1]), reverse=True)
    )

    return render(request, "core/home.html", {
        "proyectos": proyectos_destacados,
        "habilidades_por_categoria": habilidades_por_categoria,
    })


def proyectos(request):
    todos = Proyecto.objects.all()
    return render(request, "core/proyectos.html", {"proyectos": todos})


def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()
            try:
                send_mail(
                    subject=f"Portafolio — Nuevo mensaje: {mensaje.asunto}",
                    message=(
                        f"Nombre: {mensaje.nombre}\n"
                        f"Email: {mensaje.email}\n\n"
                        f"{mensaje.mensaje}"
                    ),
                    from_email=settings.EMAIL_HOST_USER or "no-reply@portafolio.local",
                    recipient_list=[settings.CONTACTO_EMAIL_DESTINO],
                    fail_silently=True,
                )
            except Exception:
                # Si el correo falla, el mensaje ya quedó guardado en la BD;
                # no rompemos la experiencia del visitante por esto.
                pass
            messages.success(request, "Mensaje enviado. Te respondo pronto.")
            return redirect("contacto")
    else:
        form = ContactoForm()
    return render(request, "core/contacto.html", {"form": form})
