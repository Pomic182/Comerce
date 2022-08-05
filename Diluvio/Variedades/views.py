from django.shortcuts import render
from Variedades.models import Variety

def create_variety(request):
    new_variety = Variety.objects.create(name='RUBIA DILUVIO', appearance='Color ámbar, rojos brillante y espuma blanca',  smell='Caramelo suave, gracias a la combinación de sus 4 maltas.', taste='Sabor maltoso, caramelo leve tostado que deja un sutil dulzor en la boca.',  marriage='El sabor de la caramelización de las maltas puede recordarnos a sabores de cebollas caramelizadas, salsas agridulces, salsas de caramelo en postres cremosos. Otros platos infalibles son las carnes rojas grilladas, hamburguesas gourmet, batatas asadas. Su sutil sabor dulce la hace perfecta para acompañar agridulces.', ibu='14.50')
    context = {
        'new_variety': new_variety
    }
    return render(request, 'new_product.html', context=context)

def list_variety(request):
    varietys = Variety.objects.all() 
    context = {
        'varietys': varietys
    }
    return render(request, 'varietys_list.html', context=context)
    
    
  