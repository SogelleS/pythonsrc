"""
导入模块
创建套接字
绑定端口和ip
开启监听设置套接字为被动模式
等待客户端链接
收发数据
关闭套接字

"""

import socket

tcp_server = socket.socket(socket.AF_INET,\
                           socket.SOCK_STREAM)
tcp_server.bind(('192.168.99.89', 6565))

tcp_server.listen(5)

# 128是最大连接数，在windows下有效
# linux下无效

new_socket,caddr= tcp_server.accept()
# 开始接收
# 返回一个套接字，和addr 组成的元组

recv_data = new_socket.recv(1024)

print(recv_data.decode())

new_socket.close()
# 不能再和当前客户端通信
# 不影响其他客户端
tcp_server.close()

