from django.contrib import admin
from django.urls import path, include
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('mercado/', include('mercado.urls')),
    path('', usuarios_views.iniciar, name='home'),
]
