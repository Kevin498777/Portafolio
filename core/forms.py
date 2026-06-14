from django import forms
from .models import Mensaje


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email':   forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'asunto':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tu mensaje...'}),
        }
