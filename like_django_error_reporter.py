# coding:utf-8
# sys.exc_info is not safe multi-thread method.
# traceback 是記錄當前 Thread 的呼叫堆疊, 所以他記錄 Sub-Multi-thread 可能會有問題。

import sys, traceback, threading, time, thread

# 模擬 Django 內部的錯誤訊息捕捉模式, 即 Error Reporting 的 logger handler。
# 利用 try-catch 的 exception 來捕捉 traceback 訊息。
def main(idx):
    for i in xrange(10):
        try:
            if i % 2 == 0:
                print i+idx + '@'  # will raise Exception
            else:
                print i+idx
        except Exception:
            # 可以告訴你哪一行錯。
            traceback.print_tb(sys.exc_info()[2])


threading.Thread(target=main, args=(1,)).start()

threading.Thread(target=main, args=(2,)).start()

time.sleep(1)

print '$'*50

# 這邊抓不到任何 traceback 因為有錯的在 Sub-Thread。
traceback.print_tb(sys.exc_info()[2])
