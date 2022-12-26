from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.core.management.base import BaseCommand
from products.models import Family

#def hola_mundo(request):
 #   return HttpResponse('Hola Mundo')

#def fecha_actual(request):
    #hoy = datetime.now().date()
    #return HttpResponse(f'La fecha de hoy es {hoy}')

#def vista_con_edad(request, edad):
    #return HttpResponse(f'Esto funciona? la edad es {edad}')

#def vista_con_template(request):
    #return render(request, 'template.html', context={})

#def saludo_desde_template(request):
    #context = {
     #   'nombre': 'maxi',
     #   'edad': 29,
      #  'usa_lentes': True,
       # 'lista_frutas': ['manzana','pera', 'naranja', 'banana'], 
    #}
    #return render(request, 'saludo.html', context=context)

def family_list(request):
    family_members = Family.objects.all()
    print("family_members",family_members)
    return render(request, 'familiares.html', {'family_members': family_members})

