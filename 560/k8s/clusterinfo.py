# ！/usr/bin/python
import json
from urllib.request import urlopen

urlAddress = 'http://192.168.8.191:8082/api/v1/model/namespaces/default/pods/'

pageInfo = urlopen(urlAddress).read().defaultecode('utf-8')
print(type(pageInfo))
# print(pageInfo)
clusterInfo = list(pageInfo)

# print(pageInfo.replace('\n', '').replace('[', '').replace(']', ''))

list_1 = pageInfo.replace('\n', '').replace('[', '').replace(']', '').replace(' ', '').replace('"', '').split(',')
print(list_1)

list_1.sort()

print(list_1)

# for item in list_2:
#     print(item)

# for item in list_1:
#     print(item)

for item in list_1:
    urlAddressMem = urlAddress + item + '/metrics/memory/usage'
    memInfo = urlopen(urlAddressMem).read().decode('utf-8')
    dict_1 = json.loads(memInfo)
    # print(item, " : ", round(float(2962448384 / 1024 / 1024 / 1024), 2))
    print(item, ":",
          round(float(int((dict_1['metrics'][len(dict_1['metrics']) - 1])['value']) / 1024 / 1024 / 1024), 3), "G")

# print(memInfo)

# dict_1 = json.loads(memInfo)

# print((dict_1['metrics'][len(dict_1['metrics']) - 1])['value'])

# print(memInfo.replace('\n', '').replace('\r', '').replace(' ', ''))
# print(round(float(2962448384/1024/1024/1024), 2))

# dict_1 = dict(memInfo.replace('\n', '').replace('\r', '').replace(' ', ''))
#
# print(dict_1)

# print(pageInfo.split('\n'))
#
#
# print(pageInfo.splitlines())
# print(type(clusterInfo))
# print(clusterInfo)
# for item in clusterInfo:
#     print(item)
