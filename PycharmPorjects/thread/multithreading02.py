#coding=utf-8
from time import sleep,ctime
from threading import Thread

def super_player(fn,time):
    for i in range(2):
        print 'Start playing:%s ! %s'%(fn,ctime())
        sleep(time)

#播放的文件名和时长
dicts = {u'算什么男人.mp3':3,u'战狼2.mp4':5,u'loadrunner视频.mp4':1}

threads = []
threadnum = range(len(dicts))

for fn,time in dicts.items():
    t = Thread(target=super_player,args=(fn,time))
    threads.append(t)

if __name__=='__main__':
    for t in threadnum:
        threads[t].start()
    for t in threadnum:
        threads[t].join()
    print 'the ending time:%s'%ctime()