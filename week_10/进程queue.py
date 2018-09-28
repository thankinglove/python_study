import time

__author__ = "Alex Li"

from multiprocessing import Process, Queue
import threading


# import queue

# def f(q):
#     q.put([42, None, 'hello'])

def f(qq):
    print("in child:", qq.qsize())
    qq.put([42, None, 'hello'])
    time.sleep(5)
    print("child:", qq.get_nowait())


if __name__ == '__main__':
    q = Queue()
    q.put("test123")
    # p = threading.Thread(target=f,)
    p = Process(target=f, args=(q,))
    p.start()
    p.join()
    # q.put(10)
    print("444", q.get_nowait())
    print("444", q.get_nowait())
    # prints "[42, None, 'hello']"
    # print(q.get())  # prints "[42, None, 'hello']"
    print("end")
