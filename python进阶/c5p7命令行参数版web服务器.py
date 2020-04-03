"""
使用c5p6的模块和主程序框架
使用sys.argv获取命令行参数 没有括号
sys.argv返回包含命令行参数的列表

eg:
**************************************************************************************
PS E:\pythonsrc\python进阶> python .\c5p7命令行参数版web服务器.py sss 666 888
['.\\c5p7命令行参数版web服务器.py', 'sss', '666', '888']
**************************************************************************************

获取端口号
而且还要检测参数个数与格式是否正确
数字格式    在(1024-65535)之间




"""

import sys
import socket
import c5p6模块化web服务器app模块 as app


class Webserver(object):

    def __init__(self,port):
        server_socker = socket.socket(socket.AF_INET, \
                                      socket.SOCK_STREAM)
        server_socker.setsockopt(socket.SOL_SOCKET, \
                                 socket.SO_REUSEADDR,
                                 True)
        server_listen_addr = ('', port)
        server_socker.bind(server_listen_addr)
        server_socker.listen(5)
        self.tcp_web_server = server_socker
        print('server inited')

    def startserver(self):

        while True:

            new_client_socket, new_client_addr = self.tcp_web_server.accept()

            self.requ_hander(new_client_socket, new_client_addr)

        self.tcp_web_server.close()

    def requ_hander(self,new_client_socket, new_client_addr):  # 接收信息并且响应
        requ_data = new_client_socket.recv(1024)
        if not requ_data:
            pass
        else:
            resp_data = app.application(requ_data,new_client_addr)
            new_client_socket.send(resp_data)
        print('响应完成')
        new_client_socket.close()


if __name__ == '__main__':

    argv_list=sys.argv
    if len(argv_list) != 2:
        print('use %s port',argv_list[0])
        exit(0)

    if not argv_list[1].isdigit():
        print('port must is digit')
        exit(0)

    port = int(argv_list[1])

    if port > 65535 or port < 1024:
        print('port must in (1024-65535)')
        exit(0)

    ser = Webserver(port)
    ser.startserver()
