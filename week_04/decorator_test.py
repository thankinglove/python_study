#!/usr/bin/env python

# import time
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time()
#         print('run time is %s ' % (stop - start))
#         # print(timeout)
#
#     return wrapper
#
#
# @decorator
# def test(list_test):
#     for i in list_test:
#         time.sleep(0.1)
#         print('-' * 20, i)
#
#
# # decorator(test)(range(10))
# test(range(10))
#
# x = 1
#
# def test():
#     print('from the module module_a', x)


# def consumer(name):
#     print("%s 准备吃包子啦!" % name)
#     while True:
#         baozi = yield
#
#         print("包子[%s]来了,被[%s]吃了!" % (baozi, name))
#
#
# c = consumer("ChenRonghua")
# c.__next__()
#
# b1 = "韭菜馅"
# c.send(b1)
# a1 = "a111"
# c.send(a1)
# a2 = "a222"
# c.send(a2)
# a3 = "a333"
# c.send(a3)
# c.__next__()
from functools import reduce

a = bytes('abcde', encoding='utf-8')
print(a.capitalize(), a)

b = bytearray('abcde', encoding='utf-8')
# print(b)
print(b.capitalize(), b)
b[0] = 200
print(b.capitalize(), b)


def func():
    pass


def func2():
    pass


print(callable(func))

print(chr(65))
print(chr(97))
print(chr(9999))

print(ord('d'))
print(ord(chr(65)))
print(ord(chr(97)))
print(ord(chr(9999)))


@classmethod
def fun1():
    pass


########################################################

x = 'for item in [1, 2, 3, 4]: print(item)'
c = compile(x, '', 'exec')
exec(c)

y = '1 + 3 / 2 * 6'
d = compile(y, '', 'eval')
print(eval(d))

z = '''
def fib(num):  # 10
    n, a, b = 0, 0, 1
    while n < num:  # n<10
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return '---done---'
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
'''
e = compile(z, "err.log", 'exec')
exec(e)
exec(z)

########################################################

print(complex(4, 4))

########################################################

# delattr()

########################################################


a = {}
print(dir(a))

########################################################

print(divmod(5, 2))

########################################################

m = 1
print(eval('m + 1'))


########################################################

# print(exec(z))


########################################################


def say(n):
    print(n)
    return True


print(say(3))

mm = say(5)
print(mm)

# print(print((lambda n_1: n_1)(5)))


########################################################

func5 = lambda max_num, min_num: max_num if max_num > min_num else min_num

print(func5(6, 3))

res = filter(lambda n: n > 5, range(10))
for i in res:
    print(i)

res = map(lambda n: n ** 2, range(10))  # [n **2 for n in range(10)]
for i in res:
    print(i)

res = [n ** 2 for n in range(10)]
for i in res:
    print(i)

print(reduce(lambda x1, y1: x1 * y1, range(1, 4), 10))

########################################################

a1 = set([1, 2, 3, 44, 55, 1, 44])
print(a1)
a1 = frozenset([1, 2, 3, 44, 55, 1, 44])
print(a1)

dict1 = globals()
print(dict1)

print('########################################################')
for item in dict1.keys():
    print("item: %s, value: %s" % (item, dict1[item]))

########################################################

print(hex(100))
print(oct(100))


def test():
    local_var = 333
    print(locals())


test()

print(locals())

########################################################

print(round(4.5))
print(round(4.6))
print(round(-4.5))
print(round(-4.6))

print(round(4.55, 1))
print(round(4.56, 1))
print(round(-4.55, 1))
print(round(-4.56, 1))

########################################################


# help(slice)

print(slice(range(10)))

print(slice(0, 10, 2))

########################################################


sort_a = [2, 4, 1, 5]

print(sorted(iter(sort_a)))

# help(sorted)

sort_dict_a = {6: 2, 8: 0, 1: 4, -5: 6, 99: 11, 4: 22}
print(sorted(sort_dict_a.items()))
# print(type(print(sorted(sort_dict_a.items()))))
print(sorted(sort_dict_a.items(), key=lambda values: values[1]))

########################################################

help(zip)

zip_a = [1, 2, 3, 4, 5, 6]
zip_b = ['a', 'b', 'c', 'd']

for i in zip(zip_a, zip_b):
    print(i)


# print(zip(iter(zip_a), iter(zip_b)))


def testFun(**args):
    print(args)


def testFun_2(*args, **kargv):
    print(args)
    print(kargv)


def testFun_3(*args, job='doctor', **kargv):
    print(args)
    print(job)
    print(kargv)


testFun(name='aming', age=10, sex='M')

testFun_2('func', name='aming', age=10, sex='M')

testFun_3('func', name='aming', age=10, sex='M')

testFun_3('func', job='kk', name='aming', age=10, sex='M')

testFun_3(job='gg', name='aming', age=10, sex='M')

