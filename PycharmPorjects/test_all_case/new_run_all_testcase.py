#coding=utf-8
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(file_new):
    #发信邮箱
    mail_from = 'pan_luluy@163.com'
    #收信邮箱
    mail_to = 'pan_luluy@163.com'
    #定义正文
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=u"百度自动化测试报告"
    #定义发送时间
    msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    #连接SMPT服务器
    smtp.connect('smtp.163.com')
    smtp.login('pan_luluy@163.com','pll19901230')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'email has send out'

def get_new_file(files):
    #定义文件目录
    lists = os.listdir(files)
    #重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn:os.path.getmtime(files+"\\"+fn))
    print u'最新的文件为：'+lists[-1]
    file_ = os.path.join(files,lists[-1])
    return file_

#定义测试文件查找目录
test_dir = r'D:\\PycharmPorjects'
#testlist得到的就是文件名.类名.方法名，所以后面可以直接run(testlist),执行test开头的py文件
testlist = unittest.defaultTestLoader.discover(test_dir,pattern='baidu*.py')


if __name__ == '__main__':
    test_report = './report/'
    now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + now_time + 'result.html'
    fp = open(filename,'wb')

    runner = HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',
                            description=u'用例执行环境Windows 7，Firefox')
    runner.run(testlist)
    fp.close()
    #调用get_new_file方法
    file_new = get_new_file(test_report)
    print file_new
    send_mail(file_new)
'''
<unittest.suite.TestSuite
tests=[<unittest.suite.TestSuite
tests=[<testadd.TestAdd testMethod=test_add0>,
       <testadd.TestAdd testMethod=test_add1>]>]>
'''