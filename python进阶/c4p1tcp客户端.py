"""
导入套接字模块
创建套接字（tcp）
建立连接
发送数据
关闭套接字

"""
import socket

stcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

addr = ('192.168.99.127',62111)

stcp.connect(addr)

stcp.send('你好'.encode())

res = stcp.recv(1024)

print(res.decode())

stcp.close()




