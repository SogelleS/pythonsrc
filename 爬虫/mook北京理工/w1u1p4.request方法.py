
'''

request.request(method, url, **kwargs)

methor      对应7种方法
url         链接
**kwargs    13个控制访问参数均为可选项

控制访问参数：
params      字典或者字节序列，作为参数添加到url中


'''
import requests

kv = {'key1': 'val1', 'key2': 'val2'}

# params      字典或者字节序列，作为参数添加到url中

r = requests.request('GET', 'http://www.baidu.com', params=kv)
print(r.url)


# http://baidu.com/?key1=val1&key2=val2
pxs = {'https':'http://127.0.0.1:1082'}

# data       字典，字节序列，文件对象作为requests的内容
# json      作为内容部分提交
r = requests.request('POST', 'http://httpbin.org/post', data=kv, proxies=pxs)
print(r.text)
r = requests.request('POST', 'http://httpbin.org/post', json=kv)
print(r.text)


# headers      字典，定制的HTTP头
hd = {'user-agent':'Chrome/10'}
r = requests.request('POST', 'http://httpbin.org/post', headers=hd)
print(r.text)


# cookies         字典，解析cookie
# auth            元组，支持http认证功能
# files           字典类型，用来传输文件
# timeout         设定超时时间 秒为单位
# proxies         字典 设定代理服务器，可以增加认证
# allow_redirects 重定向开关
# stream          获取内容立即下载开关
# verify          认证ssl证书开关
# cert            本地ssl证书路径


