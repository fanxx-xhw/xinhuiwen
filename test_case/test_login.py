import unittest
from page.page import Page

class test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page()
        # log.debug()
        cls.page.open('http://www.lawnewscn.com/')

        # cls.page.max_window()

    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_a_login(self):
        self.page.max_browser()
        self.page.login_pop()
        self.assertTrue(self.page.check_pop(self.test_a_login.__name__))