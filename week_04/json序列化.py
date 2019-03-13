__author__ = "Alex Li"
#import json

import pickle


def sayhi(name):
    print("hello,",name)


info = {
    'name':'alex',
    'age':22,
    'func':sayhi
}


f = open("test.text","wb")
#print(json.dumps(info))
print()
data = pickle.dumps(info)
print(data)
f.write(data)
# f.write( pickle.dumps( info) )

f.close()


mess = pickle.loads(data)
print(mess)

# 序列化和反序列化查看下列文档资料
# https://www.cnblogs.com/abobo/p/8080447.html