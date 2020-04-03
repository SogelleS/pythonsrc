import sys
import socket
import c5p8多网页切换app模块 as app


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

        html_dec = {
            '1': "moban1",
            '2': "moban2",
            '3': "moban3",
            '4': "moban4"
        }
        print(html_dec)
        ch = input('you choice:')
        self.daf_root_path = html_dec[ch]
        print('server inited')

    def startserver(self):

        while True:

            new_client_socket, new_client_addr = self.tcp_web_server.accept()

            self.requ_hander(new_client_socket, new_client_addr,self.daf_root_path)

        self.tcp_web_server.close()

    def requ_hander(self,new_client_socket, new_client_addr,daf_root_path):  # 接收信息并且响应
        requ_data = new_client_socket.recv(1024)
        if not requ_data:
            pass
        else:
            resp_data = app.application(requ_data,new_client_addr,daf_root_path)
            new_client_socket.send(resp_data)
        new_client_socket.close()
        print('响应完成,链接已断开')


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