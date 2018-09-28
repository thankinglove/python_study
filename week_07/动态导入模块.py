__author__ = "Alex Li"

# libaa  = __import__('lib.aa')
# object = libaa.aa.C()
# print(object.name)


# 同上面功能一样
import importlib
aa = importlib.import_module('lib.aa')
c = aa.C()
print(c.name)
