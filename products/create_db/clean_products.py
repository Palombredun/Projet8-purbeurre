import json

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
    clean_products()