from django.test import TestCase

from products.models import Category, Product

class ProductPageTes():
	def test_uses_product_page(self):
		product_ = Product.objects.create()
		response = self.client.get('/produit/%d' %(product_.id))
		self.assertTemplateUsed(response, 'products/product.html')
