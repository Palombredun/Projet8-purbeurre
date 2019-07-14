from django.urls import path
from . import views

urlpatterns = [
	path('Favoris/', views.favourites, name='favourites')
]