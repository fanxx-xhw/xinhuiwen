from page.page import Page
import time
from lib.tool import T
import unittest
from lib.logger import logger

class Test_location(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page()
        cls.page.open('http://www.lawnewscn.com/')
        # logger.debug('打开法新网。。')
    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_locate(self):
        self.page.max_browser()
        self.assertEqual(T.huoqucity(), self.page.locate(),'地区不是%s而是%s'%(T.huoqucity(),self.page.locate()))
