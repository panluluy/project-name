#coding=utf-8
from selenium.webdriver import Remote
from time import sleep

config = {'192.168.11.56:4444':'firefox'}
          #'127.0.0.1:5555':'chrome'}

#调用Remote方法
for host,browser in config.items():
    driver = Remote(command_executor='http://'+ host + '/wd/hub',
                    desired_capabilities={'platform':'ANY',
                                          'browserName':browser,
                                          'version':'',
                                          'javascriptEnabled':True
                                          }
                    )
    driver.get('http://www.baidu.com')
    sleep(2)
    driver.quit()

'''
1、selenium server（安装jdk）
2、Chrome/Firefox
3、与主hub之间要相互ping通

#192.168.0.123 主hub的ip
java -jar selenium-server-standalone-2.53.0.jar -role hub -port 3456

#192.168.0.125  远程node的ip
java -jar selenium-server-standalone-2.53.0.jar -role node -port 5555 -hub http://192.168.0.123:3456/grid/register

#主hub控制了哪些节点
http://127.0.0.1:4444/grid/console
'''

#主hub只有一个，node节点可以有多个，远程node需要指向主hub


'''
from .firefox.webdriver import WebDriver as Firefox
from .firefox.firefox_profile import FirefoxProfile
from .chrome.webdriver import WebDriver as Chrome
from .chrome.options import Options as ChromeOptions
from .ie.webdriver import WebDriver as Ie
from .edge.webdriver import WebDriver as Edge
from .opera.webdriver import WebDriver as Opera
from .safari.webdriver import WebDriver as Safari
from .blackberry.webdriver import WebDriver as BlackBerry
from .phantomjs.webdriver import WebDriver as PhantomJS
from .android.webdriver import WebDriver as Android
from .remote.webdriver import WebDriver as Remote
from .common.desired_capabilities import DesiredCapabilities
from .common.action_chains import ActionChains
from .common.touch_actions import TouchActions
from .common.proxy import Proxy


from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver

#__init__.py文件简化导入的路径
from .chrome.webdriver import WebDriver as Chrome
from selenium.webdriver import Chrome   #两个导包结果是相同的

from selenium import webdriver
由于from .chrome.webdriver import WebDriver as Chrome 将WebDriver类导入后重命名Chrome
所以后面定义driver = webdriver.Chrome()
'''