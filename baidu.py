#coding=utf-8
import unittest
from selenium import webdriver
import time

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://www.baidu.com/'

    def test_baidu(self):
        '''the testcase is use to search webdriver'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('webdriver')
        driver.find_element_by_id('su').click()
        time.sleep(3)
        # title = driver.title
        self.assertEqual(driver.title,u"webdriver_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()