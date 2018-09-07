import unittest
from page.page import Page
import time
from lib.logger import logger

class test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page()
        # log.debug()
        cls.page.open('http://www.lawnewscn.com/')
        # logger.debug('打开法新网。。')

        # cls.page.max_window()

    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_a_login(self):
        self.page.max_browser()
        # logger.debug('最大化浏览器...')
        self.page.login_pop()
        # logger.debug('点击登录按钮出现弹窗')
        time.sleep(3)
        self.assertTrue(self.page.check_pop(self.test_a_login.__name__))

    def test_b_login(self):
        time.sleep(6)
        self.page.pop_username(17600935426)
        self.page.pop_pwd('1q2w3e4r')
        self.page.click_login()
        self.assertTrue(self.page.check_login(self.test_b_login.__name__))

    def test_c_login(self):
        time.sleep(2)
        self.page.logout()
        self.page.log_out()
        self.assertTrue(self.page.check_out(self.test_c_login.__name__))