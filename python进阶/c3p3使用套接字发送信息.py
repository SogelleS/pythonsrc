import socket
# 导入模块
udptest = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 创建套接字对象

udptest.sendto('那咋办嘛'.encode(), ('192.168.99.127',8080))
# 发送数据
# 套接字对象.sentto(参数1, 参数2)
# 参数1 为数据的二进制格式 字符串.encode() 转换为2进制
# 参数2 为一个元组 (字符串类型的目标ip地址,int型的端口号)


udptest.close()
# 关闭套接字

