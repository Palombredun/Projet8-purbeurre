from django.urls import path

from . import views

urlpatterns = [
    path('Mon-Compte/', views.profile, name='profile')
]