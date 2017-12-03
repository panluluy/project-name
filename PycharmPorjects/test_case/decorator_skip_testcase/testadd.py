#coding=utf-8
import unittest
#unittest方法必须要test开头
from test_case.decorator_skip_testcase.count import Count

class TestAdd(unittest.TestCase):

    def setUp(self):
        print 'start testing-------------------------------------'

    def tearDown(self):
        print 'ending testing------------------------------------'

    # @unittest.skipIf(3 > 2,'if 3 bigger than 2 ,then skip this testcase')
    @unittest.skipUnless(3 > 2,'if 3 bigger than 2 ,then excute this testcase' )
    def test_add0(self):
        c = Count(5,6)
        self.assertEqual(c.add(),11)
        print 'i am the first testcase'

    # @unittest.skip("skip this testcase")
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