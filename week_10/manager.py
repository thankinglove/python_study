__author__ = "Alex Li"

from multiprocessing import Process, Manager
import os


def f(dd, lst):
    # dd[1] = '1'
    # dd['2'] = 2
    dd["pid%s" % os.getpid()] = os.getpid()
    lst.append(os.getpid())
    print(lst, dd)
    print(os.getpid(), "#########################################")


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()

        # ll = manager.list(range(5))
        ll = manager.list()

        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, ll))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        ll.append("from parent")
        print(d)
        print(ll)
