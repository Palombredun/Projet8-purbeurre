from django.shortcuts import render

from .models import Product

def product(request, id):
	product = Product.objects.filter(id=id)
	return render(request, 'products/product.html', {'product': product})
