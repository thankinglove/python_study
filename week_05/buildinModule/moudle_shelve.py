#! /usr/bin/env python

# https://www.cnblogs.com/frankzs/p/5949645.html

# https://blog.csdn.net/laodengbaiwe0838/article/details/52369777

import shelve

s = shelve.open('test_shelf.db')
try:
    s['key1'] = {'int': 10, 'float':9.5, 'string':'Sample data'}
finally:
    s.close()


s = shelve.open('test_shelf.db')
try:
    existing = s['key1']
    print(existing)
finally:
    s.close()


s = shelve.open('test_shelf.db', 'r')
try:
    existing = s['key1']
    print(existing)
finally:
    s.close()


s = shelve.open('test_shelf.db')
try:
    print(s['key1'])
    s['key1']['new_value'] = 'this was not here before'
finally:
    s.close()


s = shelve.open('test_shelf.db',  writeback=True)
try:
    print(s['key1'])
finally:
    s.close()


s = shelve.open('test_shelf.db', writeback=True)
try:
    print(s['key1'])
    s['key1']['new_value'] = 'this was not here before'
    print(s['key1'])
finally:
    s.close()


s = shelve.open('test_shelf.db',  writeback=True)
try:
    print(s['key1'])
finally:
    s.close()