#coding=utf-8
from time import sleep,ctime

def music(func,loop):
    for i in range(loop):
        print 'i am listening to music %s ! %s'%(func,ctime())
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print 'i am watching movic %s ! %s'%(func,ctime())
        sleep(5)

if __name__=='__main__':
    music(u'十年',2)
    music(u'速度与激情8',3)
