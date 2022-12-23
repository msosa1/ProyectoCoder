"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from django_project.views import hola_mundo, fecha_actual, vista_con_edad, vista_con_template, saludo_desde_template

from products.views import create_product, list_products,create_category, list_categories



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hola/', hola_mundo ),
    path('fecha/', fecha_actual),
    path('edad/<int:edad>/', vista_con_edad),
    path('vista_con_template/', vista_con_template),
    path('saludo_desde_template/', saludo_desde_template),
    
    path('create-product/', create_product),
    path('list-product/', list_products),
    
    path('create-category/<str:name/', create_category),
    path('list-category/', list_categories),
    
]
