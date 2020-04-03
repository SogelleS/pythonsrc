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

        new_client_socket.close()
        print('响应完成,链接已断开')


if __name__ == '__main__':

    ser = Webserver(8080)
    ser.startserver()


