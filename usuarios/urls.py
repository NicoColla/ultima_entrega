from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.iniciar_sesion, name='login'),
    path('register/', views.registrarse, name='register'),
    path('logout/', views.cerrar_sesion, name='logout'),
]
