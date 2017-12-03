#coding=utf-8
import unittest
from selenium import webdriver
import time
from HTMLTestRunner import HTMLTestRunner

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
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(Baidu("test_baidu"))

    now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = './report/' + now_time + 'result.html'
    fp = open(filename,'wb')

    runner = HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行环境Windows 7，Firefox')
    runner.run(suite)
    fp.close()