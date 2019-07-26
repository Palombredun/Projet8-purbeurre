from django.test import TestCase, Client

class FavoritePageTest(TestCase):
	def test_uses_favorite_template_logged_in(self):
		c = Client()
		response = c.post('/utilisateur/connexion/', 
			{'username': 'user', 'password': 'userpassword'})
		response = c.get('/utilisateur/favoris/')
		print(response.status_code)
		self.assertTemplateUsed(response, 'favorites/favorites.html')