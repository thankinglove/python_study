__author__ = "Alex Li"
# import module_test


from module_test import test as test


def logger():
    test()
    print('in the logger')


def search():
    test()
    print('in the search')


logger()
search()