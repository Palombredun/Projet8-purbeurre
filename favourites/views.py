from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from products.models import Product

@login_required
def favourites(request):
    current_user = {'user': request.user}
    if request.method == 'POST':
        id_product = request.POST['id_product']
        product = Product.objects.filter(id=id_product)
        new_favourite = UserProfile(current_user, product)
    return render(request, 'favourites/favourites.html', current_user)