#coding=utf-8
import unittest
#unittest方法必须要test开头
from Python_assert.count import Count


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
    unittest.main()