from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mercado import views as mercado_views

urlpatterns = [
    path('', mercado_views.inicio, name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('mercado/', include('mercado.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)