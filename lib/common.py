from lib.pyse import Pyse
from testdata.testdata import Url_Data,Login_data,Reg_data
import nnlog
import time
from lib.path import CASELOG

class Common(object): #公共方法

    #实例化pyse,并把浏览器最大化
    def __init__(self):
        self.pyse = Pyse('chrome')
        self.pyse.max_window()
        self.log = nnlog.Logger(file_name=CASELOG)

    #适用于登录页面的手机号密码登录
    def username(self):#获取用户名
        css = 'css=>[name="username"]'
        text = Login_data.username()
        # print(text)

        self.pyse.type(css,text)
        # self.log.info('正在输入密码%s' % text + '....')
    # 获取密码
    def pwd(self):#获取密码
        css = 'css=>[name="password"]'
        text = Login_data.pwd()
        self.pyse.type(css,text)
        # self.log.info('正在输入密码%s' % text + '....')
    #点击登录
    def login_btn(self): #点击登录安扭
        css = "css=>[name='login-btn']"
        self.pyse.click(css)
        # self.log.info('点击登录...')
    # 点击退出
    def check_logout(self,name):#查询到登出链接，判断是否登录成功
        css = 'css=>#signOut'
        return self.pyse.wait_and_save_exception(css,name)

     #打开登录页面

    #打开登录页
    def open_login_url(self):
        self.pyse.open(Login_data.loginUrl())
        self.log.debug('正在打开登录页面'+Login_data.loginUrl())

    #打开汇桔网主页
    def open_home_page(self):
        self.pyse.open(Url_Data.url())
        self.pyse.max_window()

        self.log.debug("正在打开汇桔云主页"+Url_Data.url())


if __name__=="__main__":
    C = Common()
    C.open_home_page()