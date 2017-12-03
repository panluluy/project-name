#coding=utf-8
from selenium import webdriver

host = 'http://127.0.0.1:4444/wd/hub'

dr = webdriver.Remote(command_executor=host,
                      desired_capabilities={'platform':'ANY',
                                          'browserName':'chrome',
                                          'version':'',
                                          'javascriptEnabled':True
                                          }
                      )
#此处换成phantomjs,需要相应的驱动，但是不会启动浏览器，执行效率高，做爬虫可以使用这种方法

#desired_capabilities在selenium\webdriver\common目录下
dr.get("http://www.baidu.com")
dr.find_element_by_name('wd').send_keys('selenium grid2')
dr.find_element_by_id('su').click()

dr.quit()

'''
#selenium grid ---分布式
#selenium server （grid2） --jar  --jdk
#webdriver.Firefox
#webdriver.Chrome  ----继承Remote()
#Remote()   ---可配置(host,browseName)
#selenium server 包含的驱动htmlunit、Safari
'''