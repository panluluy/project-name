#coding=utf-8
import unittest

def setUpModule():
    print 'test Module start >>>>>>>>>>>>>>>>>>>>>>>>>>>'

def tearDownModule():
    print 'test Module ended >>>>>>>>>>>>>>>>>>>>>>>>>>>'

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'test class start >>>>>>>>>>>>'

    @classmethod
    def tearDownClass(cls):
        print 'test class ended >>>>>>>>>>>>'

    def setUp(self):
        print 'test case start =====>'

    def tearDown(self):
        print 'test case ended =====>'

    def test_case1(self):
        print 'test case1 start--->'

    def test_case2(self):
        print 'test case2 start--->'

if __name__ == '__main__':
    unittest.main()
