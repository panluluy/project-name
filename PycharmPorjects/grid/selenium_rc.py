#coding=utf-8
from selenium.selenium import selenium
import unittest,time,re

class serc(unittest.TestCase):

    def setUp(self):
        self.sel = selenium('127.0.0.1',4444,'*firefox','https://www.baidu.com')
        self.sel.start()

    def test_serc(self):
        sel = self.sel
        sel.open('/')
        sel.window_maximize()
        sel.type('id=kw','selenium grid')
        sel.click('id=su')
        sel.wait_for_page_to_load('30000')
        time.sleep(5)

    def tearDown(self):
        self.sel.stop()

if __name__ == '__main__':
    unittest.main()