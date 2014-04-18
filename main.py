# coding:utf-8
# sys.exc_info is not safe multi-thread method.

import sys, traceback, threading, time, thread

lock = thread.allocate_lock()

def main(idx):
    print idx
    try:
        for i in xrange(10):
            if i % 2 == 0:
                print i+idx + '@'  # will raise Exception
            else:
                print i+idx
    except:
        lock.acquire()
        print '#'*80
        print threading.currentThread.__name__
        aa, bb, cc = sys.exc_info()
        traceback.print_tb(cc)
        print '#'*80
        lock.release()

threading.Thread(target=main, args=(1,)).start()
threading.Thread(target=main, args=(2,)).start()
threading.Thread(target=main, args=(3,)).start()
threading.Thread(target=main, args=(4,)).start()


import pdb; pdb.set_trace()
