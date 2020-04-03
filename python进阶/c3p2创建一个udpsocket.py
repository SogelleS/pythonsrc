"""
1导入 socket
2创建socket 使用ipv4 udp方式
3传递数据
4关闭套接字

"""
import socket

udptest = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcptest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 第一个参数协议类型
# socket.AF_INET ipv4
# socket.AF_INET6 ipv6
# 第二个参数传输方式
# socket.SOCK_DGRAM 使用udp
# socket.SOCK_STREAM 使用tcp

# 传输完成后关闭套接字
udptest.close()
tcptest.close()
