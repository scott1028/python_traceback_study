# coding:utf-8
# 好像不大實用的設計方式。

import sys, traceback, threading, time, thread

def myhook(tp, val, tb):
    print [tb]
    import pdb; pdb.set_trace()

# 設定好所有 Exception 的 hook
sys.excepthook = myhook

# lock = thread.allocate_lock()

def main(idx):
    for i in xrange(10):
        if i % 2 == 0:
            print i + idx + '@'  # will raise Exception
        else:
            print i + idx

threading.Thread(target=main, args=(1,)).start()
threading.Thread(target=main, args=(2,)).start()

# 將引發 myhook
a + '2'
