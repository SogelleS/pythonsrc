"""
单独开一个子线程用来接收信息
子线程应该守护主线程
子线程应该循环接收


"""
import threading
import socket


def puthelp():
    print('#'*50)
    print('''1发送 2退出''')
    print('#'*50)
    return int(input('选择：'))


def send(sock):
    ipadd = input('接收方ip：')
    ipport = int(input('接收方端口：'))
    text = input('发送的内容')
    sock.sendto(text.encode(), (ipadd, ipport))


def rec(sock):
    while True:
        res, add = sock.recvfrom(1024)
        print("来自[%s][%s]" % (add,res.decode()))


if __name__ == '__main__':

    udp_s = socket.socket(socket.AF_INET,\
                          socket.SOCK_DGRAM)
    udp_t = socket.socket(socket.AF_INET,\
                          socket.SOCK_DGRAM)
    udp_s.bind(("",8088))
    udp_t.bind(('',8089))

    # 创建子线程
    rec_th = threading.Thread(target=rec,\
                              args=(udp_t,))
    # 启动线程
    rec_th.setDaemon(True)
    rec_th.start()
    # 设置守护线程
    # [].append()

    while True:

        ch = puthelp()
        if ch == 1:
            print('发送信息')
            send(udp_s)

        else:
            print('退出')
            break

    udp_s.close()
    udp_t.close()

