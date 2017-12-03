#coding=utf-8
from time import sleep,ctime
from threading import Thread

def music(func,loop):
    for i in range(loop):
        print 'i am listening to music %s ! %s'%(func,ctime())
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print 'i am watching movic %s ! %s'%(func,ctime())
        sleep(5)

threads = []

t1 = Thread(target=music,args=(u'十年',2))
threads.append(t1)

t2 = Thread(target=movie,args=(u'速度与激情8',3))
threads.append(t2)

if __name__=='__main__':
    #启动线程
    for t in threads:
        t.start()
    #守护线程
    for t in threads:
        t.join()
    print 'the ending time :%s'%ctime()

'''
i am listening to music 十年 ! Sun Nov 12 10:58:22 2017
i am watching movic 速度与激情8 ! Sun Nov 12 10:58:22 2017
由于听歌与看电视时间间隔不一样所以后面运行时间不同步的原因
i am listening to music 十年 ! Sun Nov 12 10:58:24 2017
i am watching movic 速度与激情8 ! Sun Nov 12 10:58:27 2017
i am watching movic 速度与激情8 ! Sun Nov 12 10:58:32 2017
the ending time :Sun Nov 12 10:58:37 2017
'''