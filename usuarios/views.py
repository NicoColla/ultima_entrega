from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm
from .models import Usuario

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            contrasena = form.cleaned_data.get('contrasena')
            user = authenticate(request, email=email, password=contrasena)
            if user is not None:
                login(request, user)
                return redirect('mercado:inicio')
            else:
                form.add_error(None, 'Los datos ingresados son incorrectos, vuelva a intentarlo.')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form, 'show_buttons': False})

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['contrasena'])

            dia = form.cleaned_data['dia_nacimiento']
            mes = form.cleaned_data['mes_nacimiento']
            ano = form.cleaned_data['ano_nacimiento']

            if dia and mes and ano:
                try:
                    usuario.fecha_nacimiento = f"{ano}-{mes}-{dia}"
                except ValueError:
                    pass
                
            usuario.save()
            login(request, usuario)
            return render(request, 'usuarios/register_success.html', {'nombre': usuario.first_name, 'apellido': usuario.last_name})
    else:
        form = RegistroForm()

    return render(request, 'usuarios/register.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('mercado:perfil')
