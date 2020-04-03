
import socket,threading,os,re

class Webserver(object):

    def __init__(self):
        server_socker = socket.socket(socket.AF_INET, \
                                      socket.SOCK_STREAM)
        server_socker.setsockopt(socket.SOL_SOCKET, \
                                 socket.SO_REUSEADDR,
                                 True)
        server_listen_addr = ('', 8080)

        server_socker.bind(server_listen_addr)

        server_socker.listen(5)

        self.tcp_web_server = server_socker

        print('server inited')


    def startserver(self):

        while True:
            new_client_socket, new_client_addr = \
                self.tcp_web_server.accept()
            self.requ_hander(new_client_socket, new_client_addr)

        self.tcp_web_server.close()

    def requ_hander(self,new_client_socket, new_client_addr):  # 接收信息并且响应
        requ_data = new_client_socket.recv(1024)
        root_path = 'E:\\pythonsrc\\python进阶\\测试网页'
        if not requ_data:
            print('client 断开')
            new_client_socket.close()

        else:
            requ_path = re.search('GET (.*) HTTP', requ_data.decode('utf-8'))
            print(requ_path.group(1))
            requ_path = root_path + re.sub('/', '\\\\', requ_path.group(1))

            print('请求ip[%s]目标路径:[%s]' % (new_client_addr[0], requ_path))
            print('响应中......')
            resp_line = 'HTTP/1.1 200 OK\r\n'
            resp_hesder = 'Server:pyweb\r\n'
            resp_blank = '\r\n'
            if requ_path == 'E:\\pythonsrc\\python进阶\\测试网页\\':
                requ_path = 'E:\\pythonsrc\\python进阶\\测试网页\\index.html'
            if os.path.isfile(requ_path):
                with open(requ_path, 'rb') as fp:
                    resp_data = fp.read()
                    resp_total = (resp_line + resp_hesder + resp_blank).encode() + resp_data
                    new_client_socket.send(resp_total)


            # resp_data = "Hello World!!!"
            else:
                resp_line = 'HTTP/1.1 404 OK\r\n'
                new_client_socket.send(resp_line.encode())
            # requ_data = requ_data.decode('gbk').encode()

            print('响应完成')
            new_client_socket.close()


if __name__ == '__main__':

    ser = Webserver()
    ser.startserver()


