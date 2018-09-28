#! /usr/bin/env pythn

import shelve

db = shelve.open('shelveDict')  #打开文件
print(db['wangzhe']) #向从字典中获取键的方式一样读取内容
print(db['lijianguo'])  #结果为{'age': 25, 'name': 'lijianguo'}
db.close()  #关闭文件