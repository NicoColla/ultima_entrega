from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar, name='iniciar'),
    path('login/', views.loguearse, name='login'),
    path('register/', views.registrarse, name='register'),
]
