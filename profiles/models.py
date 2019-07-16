from django.db import models
from django.contrib.auth.models import User

from products.models import Product

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	favorites = models.ManyToManyField(Product)