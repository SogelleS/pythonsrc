'''
模拟浏览器的tcp客户端

1导入模块socket
2创建套接字
3建立连接
4拼接http协议
5发送请求报文
6接收服务器返回的内容
7显示内容
8断开连接

'''
import socket
def geturltest(url):
    c_socket = socket.socket(socket.AF_INET,\
                             socket.SOCK_STREAM)
    server_addr = (url, 8080)
    c_addr = ('',36321)
    c_socket.bind(c_addr)
    c_socket.connect(server_addr)
    requ_line = 'GET / HTTP/1.1\r\n'
    requ_header = 'Host:%s\r\n' % url
    requ_user_agent = 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36\r\n'
    requ_blank = '\r\n'
    requ_data = requ_line + \
                requ_header + \
                requ_user_agent + \
                requ_blank

    c_socket.send(requ_data.encode())

    recv_data = c_socket.recv(800000)
    print(recv_data.decode())

if __name__ == '__main__':
    geturltest('127.0.0.1')