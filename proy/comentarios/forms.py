from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor','ubicacion', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 12, 'cols': 50, 'style': 'resize:none;'}),
        }