from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.admin import admin_site
from django.contrib import admin
from . import views

urlpatterns = [
    path('', include('catalog.urls')),  # Включаем все URL-адреса каталога
    path('admin/', admin_site.urls),
    path('contacts/', include('contacts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('change-language/', views.change_language, name='change_language'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
