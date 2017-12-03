#coding=utf-8
from test_case.decorator_skip_testcase.count import Count

class Count_demo():

    def add_demo(self):
        try:
            c = Count(5,6)
            result = c.add()
            assert (result == 12), "result error"
        except Exception, e:
            print e
        else:
            print 'test pass'

if __name__ == "__main__":
    tc = Count_demo()
    tc.add_demo()
