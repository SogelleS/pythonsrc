"""
1导入socke模块
2创建套接字
3绑定端口
4发送数据
5关闭套接字

"""

import socket

socket1 = socket.socket(socket.AF_INET, \
                        socket.SOCK_DGRAM)

sadd1 = ('', 8088)
# 自己的地址可以不写
# 建议不写，当计算机有多个网卡（ip）时都能接受数据
tadd1 = ('192.168.99.127', 51842)

loadd = ('192.168.99.89', 6668)

socket1.bind(sadd1)

# 绑定端口
# socket.bind(adress)
# adress类型是一个元组（'ip',端口）

socket1.sendto('我是来自udp传输的数据'.encode('gbk'), \
               tadd1)

socket1.close()



