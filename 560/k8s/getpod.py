#! /usr/bin/env python

import json
from urllib.request import urlopen

import paramiko
import sys


def getPods(urlAddress):
    pageInfo = urlopen(urlAddress).read().decode('utf-8')
    listPods = pageInfo.replace('\n', '').replace('[', '').replace(']', '').replace(' ', '').replace('"', '').split(',')
    listPods.sort()
    return listPods


def getPodMem(urlAddress, podName, metric='/metrics/memory/usage'):
    newUrl = urlAddress + podName + metric
    memInfo = urlopen(newUrl).read().decode('utf-8')
    dictMen = json.loads(memInfo)
    return round(float(int((dictMen['metrics'][len(dictMen['metrics']) - 1])['value']) / 1024 / 1024 / 1024), 3)


print(getPods('http://192.168.8.191:8082/api/v1/model/namespaces/default/pods/'))
print(getPodMem('http://192.168.8.191:8082/api/v1/model/namespaces/default/pods/', 'admin-29207014-cnbtj'))


# def connect(host):
#     """this is use the paramiko connect the host,return conn"""
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     try:
#         ssh.connect(host, username='root', password='566560.com', allow_agent=True)
#         print(ssh)
#         return ssh
#     except Exception as e:
#         print(e.value)
#         return None
#
#
# def command(args, outpath):
#     """this is get the command the args to return the command"""
#     cmd = '%s %s' % (outpath, args)
#     print(cmd)
#     return cmd
#
#
# def exec_commands(conn, cmd):
#     """this is use the conn to excute the cmd and return the results of excute the command"""
#     inMess, outMess, errMess = conn.exec_command(cmd)
#     print("inMess: ", inMess)
#     print("outMess: ", outMess)
#     print("errMess: ", errMess)
#     results = outMess.read()
#     print("results: ", results)
#     return results
#
#
# message = exec_commands(connect('192.168.8.151'), command('-n default', 'kubectl get pods'))

# print(exec_commands(connect('192.168.8.151'), command('-n default', 'kubectl get pods')))

def sshclientExecmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    inMess, outMess, errMess = s.exec_command(execmd)
    inMess.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    result = outMess.read()
    s.close()
    print(type(result))
    print(result)
    return result


message = str(sshclientExecmd('192.168.8.165', 22, 'root', '566560.com', 'kubectl get pods -n default -o wide'), encoding="utf-8")
print(message)

list_mess = message.split('\n')
list_mess.remove('')
list_mess.reverse()
list_mess.pop()
list_mess.reverse()
print('#################################')
# print(info)
print('#################################')

print(list_mess)
print('#################################')
pod_info = []

for item in list_mess:
    new_list = item.split()
    dict_info = {'NAME': new_list[0], 'READY': new_list[1], 'STATUS': new_list[2], 'RESTARTS': new_list[3],
                 'AGE': new_list[4], 'IP': new_list[5], 'NODE': new_list[6]}
    pod_info.append(dict_info)
    print(item)

print(pod_info)

# for i in
#
# print(list_mess)


s = "你好"
print(sys.getdefaultencoding())

s_gbk = s.encode(encoding="gbk")
print(s_gbk)
print(s.encode())

gbk_to_utf8 = s_gbk.decode(encoding="gbk").encode(encoding="utf8")
print(gbk_to_utf8)
# print(s)
# s.decode()
# s.encode(encoding='unicode')
# print(s)