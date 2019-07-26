from django.test import TestCase

class ErsatzPageTest(TestCase):
	def test_uses_result_template(self):
		response = self.client.get('/Recherche/?query=coca')
		self.assertTemplateUsed(response, 'ersatz/result.html')