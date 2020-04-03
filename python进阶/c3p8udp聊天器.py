import socket


def puthelp():

    print('#'*50)
    print('''1发送 2接收 3退出''')
    print('#'*50)
    return int(input('选择：'))


def send(sock):
    ipadd = input('接收方ip：')
    ipport = int(input('接收方端口：'))
    text = input('发送的内容')
    sock.sendto(text.encode(), (ipadd, ipport))


def rec(sock):

    #ipport = int(input('监听端口：'))
    #sock.bind(('', ipport))
    res, add = sock.recvfrom(1024)
    print("来自[%s][%s]" % (add,res.decode()))


if __name__ == '__main__':

    udp_s = socket.socket(socket.AF_INET,\
                          socket.SOCK_DGRAM)

    while True:

        ch = puthelp()
        if ch == 1:
            print('发送信息')
            send(udp_s)

        elif ch == 2:
            print('接收信息')
            rec(udp_s)
        else:
            print('退出')
            break



    udp_s.close()





