#coding=utf-8
import unittest

from test_case.decorator_skip_testcase import testsub
from test_case.decorator_skip_testcase import testadd

'''
脚本用于执行test_case.decorator_skip_testcase目录下的testadd.py和testsub.py
用于用例与执行过程分离
导入需要增加__init__.py文件
'''

suite = unittest.TestSuite()
suite.addTest(testadd.TestAdd("test_add0"))
suite.addTest(testadd.TestAdd("test_add1"))

suite.addTest(testsub.TestSub("test_sub0"))

runner = unittest.TextTestRunner()
runner.run(suite)