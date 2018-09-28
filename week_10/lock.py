import time

__author__ = "Alex Li"

from multiprocessing import Process, Lock


def f(l, i):
    # l.acquire()
    print('hello world', i)
    # time.sleep(1)
    # l.release()


if __name__ == '__main__':
    lock = Lock()

    process = []
    for num in range(100):
        p = Process(target=f, args=(lock, num))
        process.append(p)
        p.start()

    for num in range(100):
        process[num].join()

    print("end")
