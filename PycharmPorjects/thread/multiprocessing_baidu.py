#coding=utf-8
import multiprocessing
from time import sleep,ctime
from selenium import webdriver

#测试用例
def test_baidu(browser,search):
    print 'start:%s'%ctime()
    print browser,search
    if browser=='ff':
        drivier = webdriver.Firefox()
    elif browser=='chrome':
        drivier = webdriver.Chrome()
    else:
        print u'browser参数有误，只能是谷歌和火狐，其他浏览器没有驱动'

    drivier.get('http://www.baidu.com')
    drivier.find_element_by_id('kw').send_keys(search)
    drivier.find_element_by_id('su').click()
    sleep(2)
    drivier.close()

if __name__=='__main__':
    #启动参数（指定浏览器与百度搜索内容）
    dicts = {'chrome':'webdriver','ff':'python'}

    threads = []
    threadnum = range(len(dicts))

    #创建线程
    for browser,search in dicts.items():
        t = multiprocessing.Process(target=test_baidu,args=(browser,search))
        threads.append(t)

    #启动线程
    for t in threadnum:
        threads[t].start()
    for t in threadnum:
        threads[t].join()
    print 'the ending time:%s'%ctime()