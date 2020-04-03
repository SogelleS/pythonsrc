"""
实现一个简单的web服务器返回固定的helloworld
1导入模块
2创建套接字
3设定地址重用
4绑定端口
5更改监听模式
6接受客户端连接
7接收客户端请求报文
8判断协议为空
9拼接响应报文
10发送响应报文
11关闭套接字

"""
import socket,threading


def requ_hander(new_client_socket):     # 接收信息并且响应
    requ_data = new_client_socket.recv(1024)
    if not requ_data:
        print('client 断开')
        new_client_socket.close()

    else:
        print(requ_data.decode('utf-8'))
        print('响应中......')
        resp_line = 'HTTP/1.1 200 OK\r\n'
        resp_hesder = 'Server:pyweb\r\n'
        resp_blank = '\r\n'


        resp_data = "Hello World!!!"
        resp_total = resp_line+resp_hesder+\
                     resp_blank+resp_data

        resp_total = resp_total.encode()
        new_client_socket.send(resp_total)
        new_client_socket.close()









if __name__ == '__main__':
    server_socker = socket.socket(socket.AF_INET,\
                                  socket.SOCK_STREAM)
    server_socker.setsockopt(socket.SOL_SOCKET,\
                             socket.SO_REUSEADDR,
                             True)
    server_listen_addr = ('',8080)

    server_socker.bind(server_listen_addr)

    server_socker.listen(5)

    print('server started')

    while True:

        new_client_socket,new_client_addr = \
            server_socker.accept()
        th = threading.Thread(target=requ_hander,\
                              args=(new_client_socket,))
        th.start()

        # requ_hander(new_client_socket)





    server_socker.close()