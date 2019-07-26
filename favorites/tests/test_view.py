from django.test import TestCase

class FavoritePageTest(TestCase):
	def test_uses_favorite_template_logged_in(self):
		self.client.login(username='user', password='userpassword')
		response = self.client.get('/utilisateur/favoris/')
		self.assertTemplateUsed(response, 'favorites/favorites.html')