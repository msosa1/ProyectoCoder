from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def hola_mundo(request):
    return HttpResponse('Hola Mundo')

def fecha_actual(request):
    hoy = datetime.now().date()
    return HttpResponse(f'La fecha de hoy es {hoy}')

def vista_con_edad(request, edad):
    return HttpResponse(f'Esto funciona? la edad es {edad}')

def vista_con_template(request):
    return render(request, 'template.html', context={})

def saludo_desde_template(request):
    context = {
        'nombre': 'maxi',
        'edad': 29,
        'usa_lentes': True,
        'lista_frutas': ['manzana','pera', 'naranja', 'banana'], 
    }
    return render(request, 'saludo.html', context=context)