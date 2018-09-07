import unittest
from page.page import Page

class Test_search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page = Page()
        cls.page.open('http://www.lawnewscn.com/')
    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_a_search(self):
        self.page.input_text('欠薪')
        self.page.click_search()
        self.assertEqual(True,self.page.check_search(),'关键词不是欠薪')
