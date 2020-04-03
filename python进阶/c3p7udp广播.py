"""


"""


import  socket

udp_b = socket.socket(socket.AF_INET, \
                      socket.SOCK_DGRAM)

udp_b.bind(('',8888))
# 套接字默认不允许发送广播
# 需要设置权限
udp_b.setsockopt(socket.SOL_SOCKET, \
                 socket.SO_BROADCAST, \
                 True)
# 三个参数 第一个表示当前套接字，第二个表示属性，第三个允许广播


# udp_b.sendto('广播测试'.encode(), \
             # ('255.255.255.255',53747))
udp_b.sendto('广播测试'.encode(), \
             ('192.168.99.255',63411))

udp_b.close()