from django.urls import path
from . import views

urlpatterns = [
    path('Favoris/', views.favorites, name='favorites')
]
