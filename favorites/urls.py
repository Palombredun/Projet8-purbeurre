from django.urls import path
from favorites.views import FavoriteView

urlpatterns = [
    path('Favoris/', FavoriteView.as_view(), name='favorites')
]
