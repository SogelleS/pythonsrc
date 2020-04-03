import requests

url = 'https://www.baidu.com'

# 发起get请求
res = requests.get(url)

# 查看响应结果
print(res)          # 返回requests对象
print('#'*100)
print(res.content)  # b'xxxx' 二进制文本流
print('#'*100)
print(res.text)     # 获取内容
print('#'*100)
print(res.content.decode('utf-8'))
print('#'*100)
print(res.headers)  # 响应头信息
print('#'*100)
print(res.status_code)  # 请求状态码
print('#'*100)
print(res.url)      # 请求的url
print('#'*100)
print(res.request.headers)  # 请求的头信息




