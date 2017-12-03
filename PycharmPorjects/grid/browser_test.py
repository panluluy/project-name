#coding=utf-8
from selenium.webdriver import Remote

#browsers = ['chrome','firefox']  #浏览器的参数化
hosts = ['chrome','firefox']

for browser in hosts:
    browser = {'browserName':browser}
    dr = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=browser)

    dr.get('http://www.baidu.com')
    dr.find_element_by_id('kw').send_keys('selenium grid2')
    dr.find_element_by_id('su').click()

    dr.quit()








