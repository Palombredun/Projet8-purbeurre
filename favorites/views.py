from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from products.models import Product

@login_required
def favorite(request):
    current_user = request.user
    if request.method == 'POST':
        id_product = request.POST['id_product']
        product = Product.objects.get(id=id_product)
        new_favorite = UserProfile(current_user, product)
        new_favorite.save()
    else:
        favorites = current_user.UserProfile.favorite.objects.all()
    return render(request, 'favorites/favorites.html', favorites)