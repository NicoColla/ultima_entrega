from django.shortcuts import render, redirect, get_object_or_404
from .models import VentaVehiculo, Comentario
from .forms import PublicarForm, ComentarioForm, RespuestaForm, FiltroBusquedaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def inicio(request):
    form = FiltroBusquedaForm(request.GET or None)
    publicaciones = VentaVehiculo.objects.all()

    if form.is_valid():
        if form.cleaned_data['tipo']:
            publicaciones = publicaciones.filter(tipo=form.cleaned_data['tipo'])
        if form.cleaned_data['marca']:
            publicaciones = publicaciones.filter(marca=form.cleaned_data['marca'])
        if form.cleaned_data['modelo']:
            publicaciones = publicaciones.filter(modelo__icontains=form.cleaned_data['modelo'])
        if form.cleaned_data['año']:
            publicaciones = publicaciones.filter(año=form.cleaned_data['año'])
        if form.cleaned_data['kilometros_max']:
            publicaciones = publicaciones.filter(kilometros__lte=form.cleaned_data['kilometros_max'])
        if form.cleaned_data['color']:
            publicaciones = publicaciones.filter(color=form.cleaned_data['color'])
        if form.cleaned_data['precio_min']:
            publicaciones = publicaciones.filter(precio__gte=form.cleaned_data['precio_min'])
        if form.cleaned_data['precio_max']:
            publicaciones = publicaciones.filter(precio__lte=form.cleaned_data['precio_max'])

    return render(request, 'barra/inicio.html', {'publicaciones': publicaciones, 'form': form})

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
    
    if request.method == 'POST':
        publicacion.delete()
        return redirect('mercado:publicaciones_usuario')
    return render(request, 'barra/configuracion/borrar_publicacion.html', {'publicacion': publicacion})

@login_required
def ver_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(VentaVehiculo, id=publicacion_id)
    comentarios = publicacion.comentarios.all() # type: ignore
    form = ComentarioForm()

    return render(request, 'barra/publicacion/ver_publicacion.html', {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'form': form
    })

@login_required
def configuracion(request):
    return render(request, 'barra/configuracion.html', {'usuario': request.user})

@login_required
def agregar_comentario(request, publicacion_id):
    publicacion = get_object_or_404(VentaVehiculo, pk=publicacion_id)
    print(f"Publicación ID: {publicacion.pk}")
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.usuario = request.user
            comentario.save()
            return redirect('mercado:ver_publicacion', publicacion_id=publicacion.pk)
    return redirect('mercado:ver_publicacion', publicacion_id=publicacion.pk)

@login_required
def responder_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    publicacion = comentario.publicacion
    if request.user != publicacion.vendedor:
        return redirect('mercado:ver_publicacion', publicacion_id=publicacion.id) # type: ignore

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.comentario = comentario
            respuesta.save()
            return redirect('mercado:ver_publicacion', publicacion_id=publicacion.id) # type: ignore

    form = RespuestaForm()
    return render(request, 'barra/publicacion/respuesta.html', {
        'form': form,
        'comentario': comentario,
        'publicacion': publicacion
    })