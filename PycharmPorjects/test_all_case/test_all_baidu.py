#coding=utf-8
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

test_dir = r'D:\\PycharmPorjects'


#testlist得到的就是文件名.类名.方法名，所以后面可以直接run(testlist),执行test开头的py文件
testlist = unittest.defaultTestLoader.discover(test_dir,pattern='baidu*.py')


if __name__ == '__main__':

    now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = './report/' + now_time + 'result.html'
    fp = open(filename,'wb')

    runner = HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',
                            description=u'用例执行环境Windows 7，Firefox')
    runner.run(testlist)
    fp.close()

'''
<unittest.suite.TestSuite
tests=[<unittest.suite.TestSuite
tests=[<testadd.TestAdd testMethod=test_add0>,
       <testadd.TestAdd testMethod=test_add1>]>]>
'''