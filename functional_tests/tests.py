from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_for_one_user(self):
        # Edith has heard about a cool new online food app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention the title of the app
        # and its motto
        self.assertIn('Pur Beurre', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('DU GRAS OUI, MAIS DE QUALITÉ !', header_text)

        # She tries the research form in the homepage :
        inputbox = self.browser.find_element_by_id('input-home')
        inputbox.send_keys('nutella')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        # Edith is sent to the page containing alternative products
        # to the one she searched (indicated in the top of the page)
        self.assertIn('Recherche', self.browser.title)
        # A message prevents her that she as to be connected if she wants
        # to save her favorite products
        message = self.browser.find_element_by_class_name('replacement').text
        self.assertIn('Vous devez avoir un compte pour sauvegarder des aliments', 
            message)

        # Disappointed by this, she leaves for now but promises
        # herself she will come back

    def test_create_account_and_visit_profile(self):
        # Edith has come back but has little time on her hand,
        # today she will only try to create an account and visit
        # the pages related to the user
        self.browser.get(self.live_server_url)

        # she clicks on the login icon in the navbar
        login = self.browser.find_element_by_class_name('login')
        login.click()
        self.assertIn('Connexion', self.browser.title)

        # Since Edith does not have an account yet, she has to create it
        # and so, click on the link at the bottom of the login form
        signup = self.browser.find_element_by_class_name('signup-link')
        signup.click()
        self.assertIn('Inscription', self.browser.title)

        # Now that she has reached the front page, she creates her account :
        username_input = self.browser.find_element_by_name('username')
        username_input.send_keys('Edith')
        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys('edith@mail.com')
        password1_input = self.browser.find_element_by_name('password1')
        password1_input.send_keys('Edithpassword')
        password2_input = self.browser.find_element_by_name('password2')
        password2_input.send_keys('Edithpassword')
        button = self.browser.find_element_by_tag_name('button')
        button.click()

        # She is redirected to the home page
        # she notices the navbar has changed, three icons have appeared
        self.assertIn('Pur Beurre', self.browser.title)
        try:
            icons = self.browser.find_element_by_tag_name('svg')
        except:
            print('NuSuchElementException')

        #She clicks on the profile page :
        profile_page = self.browser.find_element_by_class_name('profile')
        profile_page.click()
        self.assertIn('Profil', self.browser.title)
        username = self.browser.find_element_by_class_name('username').text
        self.assertEqual('Edith', username)
        email = self.browser.find_element_by_class_name('email').text
        self.assertEqual('edith@mail.com', email)

        # she now checks what the carrot icon refers to:
        favorites = self.browser.find_element_by_class_name('favorites')
        favorites.click()
        self.assertIn('Mes Favoris', self.browser.title)
        favorites = self.browser.find_element_by_class_name('no-fav').text
        self.assertEqual(
            "Vous n'avez enregistré aucun favori pour le moment.",
            favorites)

        # For now, she logs out
        logout  = self.browser.find_element_by_class_name('logout')
        logout.click()
        self.assertIn('Pur Beurre', self.browser.title)

        # She comes back later, and wants to try to same some product :
        login  = self.browser.find_element_by_class_name('login')
        login.click()

        # she logs in with her username and password :
        username = self.browser.find_element_by_name('username')
        username.send_keys('Edith')
        password = self.browser.find_element_by_name('password')
        password.send_keys('Edithpassword')
        button = self.browser.find_element_by_tag_name('button')
        button.click()

        # she is sent back to the home page, and leaves :
        self.assertIn('Pur Beurre', self.browser.title)
        