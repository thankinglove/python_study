__author__ = "Alex Li"
#客户端
import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send(msg.encode("utf-8"))
    data = client.recv(10240)
    print("recv:",data.decode())

client.close()


# Traceback (most recent call last):
#   File "D:/workspace/alex_python/week_07/socket_client.py", line 12, in <module>
#     data = client.recv(10240)
# ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。