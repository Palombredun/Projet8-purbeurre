# Generated by Django 2.2.3 on 2019-07-18 18:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favorite',
            field=models.ManyToManyField(null=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
