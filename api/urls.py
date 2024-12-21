"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import root_view, hello_world, sitemap_view, create_user, csrf_token_view


urlpatterns = [
    path("", root_view, name="root"),
    path("admin/", admin.site.urls), # Ruta del panel de administración
    path("csrf-token/", csrf_token_view, name="csrf-token"),
    path('sitemap/', sitemap_view, name='sitemap'),
    path('hello/', hello_world, name='hello-world'),
    path("users/create/", create_user, name="create-user"),  # Endpoint para crear usuario
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)