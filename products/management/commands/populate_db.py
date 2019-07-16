import json

from django.core.management.base import BaseCommand, CommandError
from products.models import Category, Product

class Command(BaseCommand):
    help = "Populate the database with the products previously downloaded."

    def handle(self, *args, **options):
        categories = [
            "aliments-d-origine-vegetale",
            "snacks",
            "boissons",
            "snacks-sucres",
            "produits-laitiers",
            "plats prepares",
            "boissons-sans-alcool",
            "viandes",
            "aliments-a-base-de-fruits-et-legumes",
            "produits-fermentes",
            "produits-laitiers-fermentes",
            "cereales-et-pomme-de-terre",
            "produits-a-tartiner",
            "biscuits-et-gateaux",
            "petits-dejeuners",
            "fromages",
            "charcuteries",
            "epicerie",
            "desserts",
            "fruits-et-produits-derives"
            ]

        with open("products/create_db/products.json", 'r') as f:
            products = json.load(f)

        for category in categories:
            current_category = Category(category_name=category)
            current_category.save()
            for elt in products:
                if elt['category_name'] == category:
                    new_product = Product(
                        product_name=elt['product_name'],
                        nutriscore=elt['nutriscore'],
                        image_url=elt['image_url'],
                        product_url = elt['product_url'],
                        category=current_category,
                        purchase_places=elt['purchase_place'],
                        energy_100g=elt['energy_100g'],
                        fat_100g=elt['fat_100g'],
                        saturated_fats_100g=elt['saturated_fat_100g'],
                        carbohydrates_100g=elt['carbohydrates_100g'],
                        sugars_100g=elt['sugars_100g'],
                        fibers_100g=elt['fiber_100g'],
                        proteins_100g=elt['proteins_100g'],
                        salt_100g=elt['salt_100g'],
                        )
                    new_product.save()