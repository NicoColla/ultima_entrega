from django.shortcuts import render, redirect, get_object_or_404
from .forms import PublicarForm
from .models import VentaVehiculo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def inicio(request):
    publicaciones = VentaVehiculo.objects.select_related('vendedor').all()
    return render(request, 'barra/inicio.html', {'publicaciones': publicaciones})

@login_required
def publicar(request):
    if request.method == 'POST':
        form = PublicarForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.vendedor = request.user
            instance.save()
            return redirect('mercado:inicio')
    else:
        form = PublicarForm()
    return render(request, 'barra/publicar.html', {'form': form})

@login_required
def publicaciones_usuario(request):
    publicaciones = VentaVehiculo.objects.filter(vendedor=request.user)
    return render(request, 'barra/configuracion/publicaciones_usuario.html', {'publicaciones': publicaciones})

@login_required
def editar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(VentaVehiculo, id=publicacion_id, vendedor=request.user)
    if request.method == 'POST':
        form = PublicarForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('mercado:publicaciones_usuario')
    else:
        form = PublicarForm(instance=publicacion)
    return render(request, 'barra/configuracion/editar_publicacion.html', {'form': form})

@login_required
def borrar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(VentaVehiculo, id=publicacion_id, vendedor=request.user)
    publicacion.delete()
    return redirect('mercado:publicaciones_usuario')

@login_required
def configuracion(request):
    return render(request, 'barra/configuracion.html', {'usuario': request.user})