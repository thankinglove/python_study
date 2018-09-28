#! /usr/bin/env pythn

import shelve

wangzhe = dict(zip(['name', 'age'], ['wangzhe', 24]))
lijianguo = dict(zip(['name', 'age'], ['lijianguo', 25]))

db = shelve.open('shelveDict')  # 打开一个文件
db['wangzhe'] = wangzhe  # 向文件中添加内容，添加方式与给字典添加键值对相同
db['lijianguo'] = lijianguo
db.close()  # 关闭文件