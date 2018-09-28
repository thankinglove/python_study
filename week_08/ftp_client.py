import hashlib

_author__ = "Alex Li"
import socket
client = socket.socket()

#client.connect(('192.168.16.200',9999))
client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("servr response:",server_response)
        client.send(b"ready to recv file")
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new","wb")
        m = hashlib.md5()
        while received_size < file_total_size:
            if file_total_size - received_size < 1024:
                size = file_total_size - received_size
            else:
                size = 1024
            data = client.recv(size)
            received_size += len(data)
            f.write(data)
            m.update(data)
         #print(file_total_size,received_size)
    else:
        print("file recv done", received_size,file_total_size)
        f.close()
        client.send("文件接收完毕，等待验证")
        md5_value = client.recv(1024)
        if md5_value.decode() == m.hexdigest():
            print("file recv correct", m.hexdigest())
        else:
            print("file recv error")


client.close()

