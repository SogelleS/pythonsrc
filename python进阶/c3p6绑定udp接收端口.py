"""
导入模块
创建套接字
绑定端口
接收数据
显示数据
关闭端口


"""

import socket

socket1 = socket.socket(socket.AF_INET, \
                        socket.SOCK_DGRAM)

sadd1 = ('192.168.99.89', 6668)
tadd1 = ('192.168.99.127', 8080)

socket1.bind(sadd1)

while True:
    test,add_port = socket1.recvfrom(1024)
    print('来自[%s]:%d' % add_port, '\n[%s]' % test.decode())
    if test.decode('gbk')[0] == 'q':
        break

socket1.close()
