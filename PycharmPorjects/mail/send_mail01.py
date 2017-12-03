#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'pan_luluy@163.com'
receiver = 'pan_luluy@163.com'
subject = 'python is very strong'
smtpserver = 'smtp.163.com'

username = 'pan_luluy@163.com'
password = 'pll19901230'

msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()