#coding=utf-8
import unittest
#unittest方法必须要test开头
from Python_assert.count import Count

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

class TestSub(unittest.TestCase):

    def setUp(self):
        print 'start testing-------------------------------------'

    def tearDown(self):
        print 'ending testing------------------------------------'


    def test_sub0(self):
        c = Count(11,6)
        self.assertEqual(c.sub(),5)
        print '5555555'



if __name__ == "__main__":
    # unittest.main()
    # #构建测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add0"))
    # suite.addTest(TestAdd("test_add1"))
    suite.addTest(TestSub("test_sub0"))

    runner = unittest.TextTestRunner()
    runner.run(suite)