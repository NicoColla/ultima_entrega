from django.shortcuts import render, redirect
from .forms import PublicarForm

def inicio(request):
    return render(request, 'barra/inicio.html')

def buscar(request):
    return render(request, 'barra/buscar.html')

def publicar(request):
    if request.method == 'POST':
        form = PublicarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mercado:inicio')
    else:
        form = PublicarForm()
    return render(request, 'barra/publicar.html', {'form': form})

def perfil(request):
    return render(request, 'barra/perfil.html')

