from django.urls import path

from . import views

urlpatterns = [
    path('Inscription/', views.signup, name='signup'),
]