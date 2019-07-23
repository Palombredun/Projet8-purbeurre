from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from products.models import Product

@login_required
def favorites(request):
    if request.method == 'POST':
        current_user = request.user
        id_product = request.POST['product_id']
        product = Product.objects.get(id=id)
        product.add(current_user)
    else:
        current_user = request.user
        favorites = Product.objects.filter(favorite__id=current_user.id)
    return render(request, "favorites/favorites.html", {'favorites': favorites})


    #if request.method == 'POST':
    #    current_user = request.user
    #    id_product = request.POST['product_id']
    #    product = Product.objects.get(id=id_product)
    #    new_favorite = User.favorites(product)
    #    new_favorite.save()
    #else:
    #    current_user = request.user
    #    user = User.objects.get(id=current_user.id)
    #    favorites = user.favorites.all()
    #return render(request, 'favorites/favorites.html', {'favorites': favorites})