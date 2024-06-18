from django.urls import path
from . import views

app_name = 'mercado'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('publicar/', views.publicar, name='publicar'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('configuracion/publicaciones/', views.publicaciones_usuario, name='publicaciones_usuario'),
    path('configuracion/publicaciones/borrar/<int:publicacion_id>/', views.borrar_publicacion, name='borrar_publicacion'),
    path('configuracion/publicaciones/editar/<int:publicacion_id>/', views.editar_publicacion, name='editar_publicacion'),
]

