#coding=utf-8
from threading import Thread
from time import sleep,ctime
from selenium import webdriver

'''
需要运行java -jar selenium-server-standalone-2.53.1.jar -role hub
java -jar selenium-server-standalone-2.53.1.jar -role node -port 5555
java -jar selenium-server-standalone-2.53.1.jar -role node -port 6666
'''
#测试用例
def test_baidu(host,browser):
    print 'start:%s'%ctime()
    print host,browser
    dc = {'browserName':browser}
    driver = webdriver.Remote(command_executor=host,
                              desired_capabilities=dc)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.close()

if __name__=='__main__':
    #启动参数（指定浏览器与主机）
    lists = {'http://127.0.0.1:5555/wd/hub':'chrome',
             'http://127.0.0.1:6666/wd/hub':'firefox'}

    threads = []
    threadnum = range(len(lists))

    #创建线程
    for host,browser in lists.items():
        t = Thread(target=test_baidu,args=(host,browser))
        threads.append(t)

    #启动线程
    for t in threadnum:
        threads[t].start()
    for t in threadnum:
        threads[t].join()
    print 'the ending time:%s'%ctime()

'''
unittest单元测试框架不支持多用例并行，建议使用多虚拟机
testNG单元测试框架很好的支持java的单元测试框架
pytest error(定位失败)，fail(断言失败)
提高web测试用例的稳定性：在设计自动化测试用例的时候，需要前端配合尽量将元素设置id属性
'''