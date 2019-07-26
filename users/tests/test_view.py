from django.test import TestCase

class LoginPageTest(TestCase):
	def test_uses_login_page(self):
		response = self.client.get('/utilisateur/connexion/')
		self.assertTemplateUsed(response, 'users/login.html')