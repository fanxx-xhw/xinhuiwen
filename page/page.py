from lib.pyse import Pyse
import time
from lib.path import WEBPICTUREPATH
class Basepage(object):
    def __init__(self):
        self.pyse = Pyse('chrome')

    def open(self,url):
        self.pyse.open(url)

    def max_browser(self):
        self.pyse.max_window()

    def quit(self):
        self.pyse.quit()

    def close(self):
        self.pyse.close()

    def switch(self):
        self.pyse.open_new_window()

class Login(Basepage):

    def login_pop(self):
        css = 'css=>[data-api="/accounts/login"]'
        self.pyse.click(css)

    def check_pop(self,name):
        css = 'css=>#login-form'
        res=self.pyse.wait_and_save_exception(css,name)
        return res

    def pop_username(self,text):
        css = 'css=>.username'
        self.pyse.type(css,text)

    def pop_pwd(self,text):
        css = 'css=>.password'
        self.pyse.type(css,text)

    def click_login(self):
        css = 'xpath=>//*[@id="login-form"]/button'
        self.pyse.click(css)

    def check_login(self,name):
        css = 'css=>.nav-username.nav-auth-btn>i'
        res=self.pyse.wait_and_save_exception(css,name)
        return res

    def logout(self):
        css = 'css=>.nav-username.nav-auth-btn>i'
        self.pyse.click(css)
        time.sleep(2)
    def log_out(self):
        css = 'css=>.logout-btn'
        self.pyse.click(css)

    def check_out(self,name):
        css = 'css=>.nav-auth'
        res = self.pyse.wait_and_save_exception(css,name)
        return res


class Search(Login):

    def input_text(self,text):
        css = 'css=>.search-input'
        self.pyse.type(css,text)
        # logger.debug('输入搜索关键字：%s'%text)

    def click_search(self):
        css = 'css=>.search-btn'
        self.pyse.click(css)
        # logger.debug('点击搜索按钮')

    def check_search(self):
        css = 'css=>.keyword'
        res = self.pyse.get_text(css)
        if res=='欠薪':
            return True
        else:
            return False

class Locate(Search):
    def locate(self):
        css = 'css=>.tpwidget_title_hook.title_2I35arv'
        res = self.pyse.get_display(css)
        if res == True:
            res = self.pyse.get_text(css)
            return res
        else:
            self.pyse.get_windows_img(WEBPICTUREPATH+'test_locate.jpg')






class Page(Locate):
    pass

if __name__=='__main__':
    p = Page()
    p.open('http://www.lawnewscn.com/')
    # p.login_pop()
    # p.pop_username(17600935426)
    # p.pop_pwd('1q2w3e4r')
    # p.click_login()
    print(p.locate())
