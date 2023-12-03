from django import forms

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar', max_length=100, required=False)