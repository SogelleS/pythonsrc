"""
导入模块
创建套接字
绑定端口
设置监听模式
等待客户端连接
接收文件名
循环读取文件内容
发送给客户端
关闭连接
关闭服务器
（多线程）

"""


def sendfile(new_c_socket,new_c_addr):
    print('welcome', new_c_addr)

    recv = new_c_socket.recv(1024).decode()
    print('file name:', recv)

    if os.path.isfile(recv):
        file_size = os.path.getsize(recv)
        new_c_socket.send(str(file_size).encode())
        with open(recv, 'rb') as filep:
            while True:
                # 循环发送1024个字节
                data = filep.read(1024)
                if data:
                    new_c_socket.send(data)
                else:
                    break
    else:
        new_c_socket.send('no file'.encode())
    new_c_socket.close()



import socket
import os,threading

service_socket = socket.socket(socket.AF_INET,\
                               socket.SOCK_STREAM)

service_addr = ('',25700)
service_socket.bind(service_addr)
service_socket.listen(5)

while True:
    new_c_socket, new_c_addr = service_socket.accept()
    th = threading.Thread(target=sendfile,args=(new_c_socket,new_c_addr))
    th.setDaemon(True)
    th.start()

service_socket.close()

