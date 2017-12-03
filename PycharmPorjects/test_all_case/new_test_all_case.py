#coding=utf-8
import unittest

test_dir = r'../test_case'


#testlist得到的就是文件名.类名.方法名，所以后面可以直接run(testlist),执行test开头的py文件
testlist = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')


if __name__ == '__main__':
    for i in testlist:
        print i

    runner = unittest.TextTestRunner()
    runner.run(testlist)

'''
<unittest.suite.TestSuite
tests=[<unittest.suite.TestSuite
tests=[<testadd.TestAdd testMethod=test_add0>,
       <testadd.TestAdd testMethod=test_add1>]>]>
'''