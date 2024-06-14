from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroForm, LoginForm
from .models import Usuario

def iniciar(request):
    return render(request, 'usuarios/base.html')

def loguearse(request):
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
    return render(request, 'usuarios/login.html', {'form': form})

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        print("Formulario recibido: ", request.POST)
        if form.is_valid():
            print("Formulario es válido")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('contrasena'))
            user.save()
            login(request, user)
            nombre = form.cleaned_data.get('first_name')
            apellido = form.cleaned_data.get('last_name')
            return render(request, 'usuarios/register_success.html', {'nombre': nombre, 'apellido': apellido})
        else:
            form.add_error(None, "Algunos datos fueron ingresados incorrectamente.")
    else:
        form = RegistroForm()
    return render(request, 'usuarios/register.html', {'form': form})
