#! /usr/bin/env pythn
# https://blog.csdn.net/laodengbaiwe0838/article/details/52369777
import shelve
db = shelve.open('shelveDict')  #打开文件
wangzhe = db['wangzhe']     #从文件中读取之前存储的对象
print(wangzhe)
wangzhe['name'] = 'wang zhe'   #直接对对象进行修改
db['wangzhe'] = wangzhe     #重新存储至字典文件对象中
print(db['wangzhe'])    #结果如下{'age': 24, 'name': 'wang zhe'}
db.close()   #关闭文件