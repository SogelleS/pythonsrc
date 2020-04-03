# 登录请求的url(post)
# https://www.hhgal.com/wp-login.php

# 登陆界面url(get)
# https://www.hhgal.com/

# 登录请求的信息
# log: sogell
# pwd: hhh2333
# submit:


import requests

url_login = 'https://www.hhgal.com/wp-login.php'
url_t = 'https://www.hhgal.com/wenzhangshoucang.html/'

# 设置请求头
userHeaders = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
# 定义post的数据
data = {
    'log': 'sogell',
    'pwd': 'hhh2333',
    'submit': ''
}


# 如果要主动记录cookie需要在requests之前调用session方法
# 并使用session方法返回的对象发送请求
req = requests.session()

res = req.post(url=url_login, headers=userHeaders,\
               data=data)
print(res.status_code)
if res.status_code==200:
    res2 = req.get(url=url_t, headers=userHeaders)
    res2.encoding = 'utf-8'
    print(res2.text)



