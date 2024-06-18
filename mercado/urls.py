from django.urls import path
from . import views

app_name = 'mercado'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('publicar/', views.publicar, name='publicar'),
    path('configuracion/', views.configuracion, name='configuracion'),
]

