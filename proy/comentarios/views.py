from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm

def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'mapap/avistamientos.html', {'comentarios': comentarios})

def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_comentarios')
    else:
        form = ComentarioForm()
    return render(request, 'comentarios/agregar_comentario.html', {'form': form})
