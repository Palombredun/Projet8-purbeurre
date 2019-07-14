from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('Connexion/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('Deconnexion/', auth_views.LogoutView.as_view(), name='logout'),
]