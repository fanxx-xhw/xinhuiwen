from lib.pyse import Pyse
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

class Yewu(Basepage):

    def login_pop(self):
        css = 'css=>[data-api="/accounts/login"]'
        self.pyse.click(css)

    def check_pop(self,name):
        css = 'css=>#login-form1'
        res=self.pyse.wait_and_save_exception(css,name)
        return res

class Page(Yewu):
    pass

# if __name__=='__main__':
#     p = Page()
#     p.open()
#     p.login_pop()
#     print(p.check_pop('a.jpg'))
