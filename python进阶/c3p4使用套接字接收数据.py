import socket
# 导入模块
udptest = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 创建套接字对象

udptest.sendto('hello world'.encode(), ('192.168.99.127',8080))
# 发送数据
# 套接字对象.sentto(参数1, 参数2)
# 参数1 为数据的二进制格式 字符串.encode() 转换为2进制
# 参数2 为一个元组 (字符串类型的目标ip地址,int型的端口号)

recv_data = udptest.recvfrom(1024)
# 1024 为缓冲区大小单位：字节
# 这个方法会造成程序自动堵塞（与input类似）
# 接收到数据会自动解除堵塞否则会一直等待
# 接收到的数据是一个元组
print(recv_data)
print(recv_data)

udptest.close()
# 关闭套接字

