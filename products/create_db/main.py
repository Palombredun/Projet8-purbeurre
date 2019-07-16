from products.create_db.dl_products import *
from products.create_db.clean_products import *

data = download_products()
clean_products(data)