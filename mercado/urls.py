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
    path('publicacion/<int:publicacion_id>/', views.ver_publicacion, name='ver_publicacion'),
    path('publicacion/<int:publicacion_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
]

