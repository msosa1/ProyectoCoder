from django.shortcuts import render
from django.http import HttpResponse

#from products.models import Products
from products.models import Family


# Create your views here.
#def create_product(request):
    #new_product = Products.objects.create(name='Coca cola 1L', price= 150, stock=False)
    #print(new_product)
    #return HttpResponse('Se creo el nuevo producto')

#def list_products(request):
    #all_products = Products.objects.all()
    #print(all_products)
    #context = {
     #   'products': all_products,
    #}
    #return render (request, 'list_products.html', context=context)
    
def family_list(request):
    family_members = Family.objects.all()
    print("family_members",family_members)
    return render(request, 'familiares.html', {'family_members': family_members})