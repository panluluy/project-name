#coding=utf-8
import unittest
#unittest方法必须要test开头
from Python_assert.count import Count

'''
单元测试框架执行指定的测试用例
'''


class TestAdd(unittest.TestCase):

    def setUp(self):
        print 'start testing-------------------------------------'

    def tearDown(self):
        print 'ending testing------------------------------------'


    def test_add0(self):
        c = Count(5,6)
        self.assertEqual(c.add(),11)
        print 'i am the first testcase'

    def test_add1(self):
        c = Count('he','llo')
        self.assertIn(c.add(),'hello world')
        print 'i am the second testcase'


if __name__ == "__main__":
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)