"""
URL configuration for restaurante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views

urlpatterns = [
    path('',include('ensueño.urls')),
    path('admin/', admin.site.urls),
    path('actividades_de_usuario/', include('actividades_de_usuario.urls')),
    path('ensueño/', include('ensueño.urls')),
    path('api_generate_token/', views.obtain_auth_token),
    

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)