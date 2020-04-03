"""
导入模块 socket
创建套接字
与服务器建立连接
用户输入文件名
发送文件名数据
创建文件准备保存（分块，循环接收）
关闭套接字

"""
import socket
from tqdm import tqdm

dow_file_socket = socket.socket(socket.AF_INET,\
                                socket.SOCK_STREAM)

addr = ('',25701)
server_addr = ('127.0.0.1',25700)
dow_file_socket.bind(addr)
dow_file_socket.setsockopt(socket.SOL_SOCKET,\
                           socket.SO_REUSEADDR, 1)

dow_file_socket.connect(server_addr)
file_name = input('enter file path:')
dow_file_socket.send(file_name.encode())

recv = dow_file_socket.recv(1024)
if recv.decode() == 'no file':
    print('service no file[%s]' % file_name)
else:
    file_size = int(recv.decode())
    if file_size/1024==0:
        file_time = file_size/1024
    else:
        file_time = int(file_size/1024) + 1
    with open('rec.file','wb') as filep:
        for i in tqdm(range(file_time),unit='KB',ncols=65):
            recv2 = dow_file_socket.recv(1024)
            filep.write(recv2)
            # if recv2:
            # # 判断是否传送完毕
            #     filep.write(recv2)
            # else:
            #     break


dow_file_socket.close()






