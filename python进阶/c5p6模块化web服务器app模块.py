import os,re


def application(requ_data,new_client_addr):

    requ_path = parsepath(requ_data)
    print('请求ip[%s]目标路径:[%s]' % (new_client_addr[0], requ_path))

    # resp_line = 'HTTP/1.1 200 OK\r\n'
    # resp_hesder = 'Server:pyweb\r\n'
    # resp_blank = '\r\n'

    if os.path.isfile(requ_path):
        status = 200
        with open(requ_path, 'rb') as fp:
            resp_data = fp.read()

    else:
        status = 404
        resp_data = 'can\'t find page'.encode('utf-8')

    resp_total = creatRespTelegram(resp_data,status)

    return resp_total


def parsepath(requ_data):

    root_path = 'E:\\pythonsrc\\python进阶\\测试网页'
    requ_path = re.search('GET (.*) HTTP', requ_data.decode('utf-8'))
    requ_path = root_path + re.sub('/', '\\\\', requ_path.group(1))

    if requ_path == 'E:\\pythonsrc\\python进阶\\测试网页\\':
        requ_path = 'E:\\pythonsrc\\python进阶\\测试网页\\index.html'

    return requ_path

# 可以将creatRespTelegram函数封装到另一个.py文件中

def creatRespTelegram(resp_body,status):

    resp_line = 'HTTP/1.1 %d OK\r\n' % status
    resp_hesder = 'Server:pyweb\r\n'
    resp_blank = '\r\n'
    return (resp_line+resp_hesder+resp_blank).encode('utf-8')+resp_body



