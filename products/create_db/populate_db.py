import requests
import json

class PopulateDB:
    def __init__(self):
        self.base_url = "https://fr.openfoodfacts.org/categorie/"
        self.categories = [
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

    def download_row_products(self):
        counter = 0
        products = [{}]
        # explore 40 pages of products and extract their name, nutriscore and image url
        for page in range(1,40):
            for category in categories:
                print(counter)
                link = base_link + category + '/' + str(page) + '.json'
                resp = requests.get(link)
                req = resp.json()
    
                j = 0 
                for _ in req['products']:
                    if 'product_name' in req['products'][j].keys() and \
                        'image_front_url' in req['products'][j].keys() and \
                        'nutrition_grade_fr' in req['products'][j].keys() and \
                        'url' in req['products'][j].keys():
    
                        try:
                            purchase_place = req['products'][j]['purchase_places']
                        except:
                            purchase_place = ''
                        try:
                            energy_100g = req['products'][j]['nutriments']['energy_100g']
                        except:
                            energy_100g = -1.
                        try:
                            fat_100g = req['products'][j]['nutriments']['fat_100g']
                        except:
                            fat_100g = -1.
                        try:
                            saturated_fat_100g = req['products'][j]['nutriments']['saturated-fat_100g']
                        except:
                            saturated_fat_100g = -1.
                        try:
                            carbohydrates_100g = req['products'][j]['nutriments']['carbohydrates_100g']
                        except:
                            carbohydrates_100g = -1.
                        try:
                            sugars_100g = req['products'][j]['nutriments']['sugars_100g']
                        except:
                            sugars_100g = -1.
                        try:
                            fiber_100g = req['products'][j]['nutriments']['fiber_100g']
                        except:
                            fiber_100g = -1.
                        try:
                            proteins_100g = req['products'][j]['nutriments']['proteins_100g']
                        except:
                            proteins_100g = -1.
                        try:
                            salt_100g = req['products'][j]['nutriments']['salt_100g']
                        except:
                            salt_100g = -1.

                        products.append({
                            'product_name': req['products'][j]['product_name'],
                            'nutriscore': req['products'][j]['nutrition_grade_fr'],
                            'image_url': req['products'][j]['image_front_url'],
                            'product_url': req['products'][j]['url'],
                            'category_name': category,
                            'purchase_place': purchase_place,
                            'energy_100g': energy_100g,
                            'fat_100g': fat_100g,
                            'saturated_fat_100g': saturated_fat_100g,
                            'carbohydrates_100g': carbohydrates_100g,
                            'sugars_100g': sugars_100g,
                            'fiber_100g': fiber_100g,
                            'proteins_100g': proteins_100g,
                            'salt_100g': salt_100g
                            })
                    j += 1
                counter += 1
                time.sleep(1)
        return products

    def is_duplicate(product_name, products_added):
    if product_name in products_added:
        return True

    def clean_products(data):
        """
        take the products tree and for each subcategory return
        a maximum of 30 products in another json file    
        """
    
        # for each product, check if it's not already in the list
        # if not, add it and its characteristics to 'cleaned_products'
        # add in a list the ids of th subcategories added
        products_added = []
        cleaned_products = []
        cat = []
        for elt in data:
            if is_duplicate(elt['product_name'], products_added) is not True:
                cleaned_products.append(elt)
                products_added.append(elt['product_name'])
    
    
        with open('products.json', 'w') as f:
            json.dump(cleaned_products, f, indent=4)

if __name__ == '__main__':
        obj = PopulateDB()
        raw_products = obj.download_row_products()    