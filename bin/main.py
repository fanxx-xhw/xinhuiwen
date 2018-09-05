import unittest
from lib.path import WEBCASEPATH,REPORTPATH
from lib.HTMLTestRunner import HTMLTestRunner
from lib.tool import Tool
class Main(object):
    def run(self):
        Tool().clear_picture()
        suit = unittest.TestSuite()
        cases = unittest.defaultTestLoader.discover(WEBCASEPATH)
        for case in cases:
            suit.addTest(case)
        f = open(REPORTPATH,'wb')
        runner = HTMLTestRunner(f, verbosity=1, title=u'测试报告', description=u'用例执行情况：')
        runner.run(suit)
        f.flush()
        f.close()
if __name__ == '__main__':
    Main().run()