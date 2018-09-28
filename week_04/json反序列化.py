__author__ = "Alex Li"


import pickle
import json


# from json序列化 import sayhi

def sayhi(name):
    print("hello2,", name)


f = open("test.text", "rb")

data = pickle.loads(f.read())

print(data)

# print(data["func"]("Alex"))
# print(data["func"]("age"))

f.close()

# info = {
#     'name': 'alex',
#     'age': 22
# }
#
# content = str(info)
# print(type(content))
#
# data2 = eval(content)
# print(type(data2))
# for key in data2.keys():
#     print(key, data2[key])

# print(json.dumps(info))
