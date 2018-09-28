#! /usr/bin/env python
# egon09.blog.51cto.com/9161406/1840425
# http://blog.51cto.com/egon09/1840425
import random

# help(random)

# help(random.random)
#
# help(random.randint)
#
# help(random.randrange)
#
# help(random.choice)
#
# help(random.choices)
#
# help(random.sample)
print(random.sample('hello world', 2))

print("random.random()", random.random())

code = ''
# for i in range(4):
#     current = random.randrange(1, 9)
#     code += str(current)
#
# print(code)

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))

for i in range(6):
    current = random.randrange(0, 6)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = chr(random.randint(97, 122))
    code += str(tmp)

print(code)

# 随机整数：
print(random.randint(0, 99))  # 70

# 随机选取0到100间的偶数：
print(random.randrange(0, 101, 2))  # 4

# 随机浮点数：
print(random.random())  # 0.2746445568079129
print(random.uniform(1, 10))  # 9.887001463194844

# 随机字符：
print(random.choice('abcdefg&#%^*f'))  # f

# 多个字符中选取特定数量的字符：
print(random.sample('abcdefghij', 3))  # ['f', 'h', 'd']

# 随机选取字符串：
print(random.choice(['apple', 'pear', 'peach', 'orange', 'lemon']))  # apple
# 洗牌#
items = [1, 2, 3, 4, 5, 6, 7]
print(items)  # [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print(items)  # [1, 4, 7, 2, 5, 3, 6]