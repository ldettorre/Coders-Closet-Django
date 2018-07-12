from django.shortcuts import render
from .models import Product

def get_products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html',{'products': products})
    
def get_mens(request):
    products = Product.objects.filter(category="MENS_TSHIRTS")  
    return render(request,"products/products.html",{'products': products})
    