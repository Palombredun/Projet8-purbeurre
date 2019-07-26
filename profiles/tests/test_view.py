from django.test import TestCase, Client

class ProfilePageTest(TestCase):
	def test_uses_profile_page_when_logged_in(self):
		c = Client()
		response = c.post('/utilisateur/connexion/', 
			{'username': 'user', 'password': 'userpassword'})
		self.assertEquals(response.status_code, 200)
		response = c.get('/utilisateur/mon-compte/')
		self.assertTemplateUsed(response, 'profiles/profile.html')