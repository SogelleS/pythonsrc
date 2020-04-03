import threading
import socket

tcp_server = socket.socket(socket.AF_INET,\
                           socket.SOCK_STREAM)
tcp_server.bind(('192.168.99.89', 6565))
tcp_server.listen(5)

while True:
    new_socket,caddr= tcp_server.accept()
    print('客户端已连接 %s' % str(caddr))

    while True:
        recv_data = new_socket.recv(1024)
        # if len(recv_data) == 0:
        # if recv_data == None: 不行
        if not recv_data:
        # 如果非空即为真
            print('客户端断开 %s' % str(caddr))
            new_socket.close()
            break
        else:
            print(recv_data.decode())


tcp_server.close()

