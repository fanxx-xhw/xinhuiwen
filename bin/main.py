import unittest
from lib.path import WEBCASEPATH,REPORTPATH
from lib.HTMLTestRunner import HTMLTestRunner
from lib.tool import T
import datetime
class Main(object):
    def run(self):
        T.clear_picture()
        suit = unittest.TestSuite()
        cases = unittest.defaultTestLoader.discover(WEBCASEPATH)
        for case in cases:
            suit.addTest(case)
        f = open(REPORTPATH,'wb')
        runner = HTMLTestRunner(f, verbosity=1, title=u'测试报告', description=u'用例执行情况：')
        runner.run(suit)
        f.flush()
        f.close()
        T.send_email('2758074764@qq.com','fanxiangxiang@huikecloud.com','auto_test_report','日期：%s'%datetime.datetime.today().strftime('%Y%m%d%H%M%S'),r'G:\xinhuiwen\report\report.html')

if __name__ == '__main__':
    Main().run()