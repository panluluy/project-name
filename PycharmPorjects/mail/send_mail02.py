#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'pan_luluy@163.com'
receiver = 'pan_luluy@163.com'
subject = 'python is very strong'
smtpserver = 'smtp.163.com'

username = 'pan_luluy@163.com'
password = 'pll19901230'

msgRoot = MIMEMultipart('related')
#邮件主题
msgRoot['Subject'] = 'python email test'
#构造附件
att = MIMEText(open('D:\\PycharmPorjects\\mail\\testdemo.txt','rb').read(),'base64','utf-8')
att['Content-Type'] = 'application\octet-stream'
att['Content-Disposition'] = 'attachement;filename=testdemo.txt'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()