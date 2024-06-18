from django.urls import path
from . import views

app_name = 'mercado'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('publicar/', views.publicar, name='publicar'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/publicaciones/', views.publicaciones_usuario, name='publicaciones_usuario'),
    path('perfil/publicaciones/borrar/<int:publicacion_id>/', views.borrar_publicacion, name='borrar_publicacion'),
    path('perfil/publicaciones/editar/<int:publicacion_id>/', views.editar_publicacion, name='editar_publicacion'),
    path('publicacion/<int:publicacion_id>/', views.ver_publicacion, name='ver_publicacion'),
    path('publicacion/<int:publicacion_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('comentario/<int:comentario_id>/respuesta/', views.responder_comentario, name='respuesta'),
]

