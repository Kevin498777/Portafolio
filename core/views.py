from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Proyecto, Habilidad, Mensaje
from .forms import ContactoForm


def home(request):
    proyectos_destacados = Proyecto.objects.filter(destacado=True)[:3]
    habilidades = Habilidad.objects.all()

    habilidades_por_categoria = {}
    for h in habilidades:
        cat = h.get_categoria_display()
        habilidades_por_categoria.setdefault(cat, []).append(h)

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
            form.save()
            messages.success(request, "Mensaje enviado. Te respondo pronto.")
            return redirect("contacto")
    else:
        form = ContactoForm()
    return render(request, "core/contacto.html", {"form": form})
