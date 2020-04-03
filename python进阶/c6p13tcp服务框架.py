"""
导入模块socket threading
创建套接字
设置端口重复使用
绑定端口
设置套接字————>被动模式
等待连接创建子线程
等待发送接收信息
关闭客户端关闭子线程


"""
import threading
import socket


def recv_sock_text(sock,addr):
    while True:
        recv_new_data = sock.recv(1024)
        if recv_new_data:
            recv_new_text = recv_new_data.decode()
            print(recv_new_text, '来自 ', \
                  addr[0], addr[1])
        else:
            print(addr,'已断开')
            break




if __name__ == '__main__':
    tcp_ss = socket.socket(socket.AF_INET, \
                           socket.SOCK_STREAM)

    port = 8888
    server_addr = ('',port)
    tcp_ss.bind(server_addr)

    tcp_ss.setsockopt(socket.SOL_SOCKET, \
                      socket.SO_REUSEADDR, 1)

    tcp_ss.listen(10)

    while True:
        new_c_socket,new_c_addr = tcp_ss.accept()
        print('[%s]port:%d已连接' %\
              (new_c_addr[0],new_c_addr[1]))

        new_c_th = threading.Thread(target=recv_sock_text,\
                                    args=(new_c_socket,new_c_addr))
        new_c_th.setDaemon(True)
        new_c_th.start()

    new_c_socket.close()




