import requests
url = 'https://www.amazon.cn/dp/B073DK1VMZ'

# 定义请求头信息

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

res = requests.get(url, headers=hd)
#res.encoding = 'utf-8'

print(res.status_code)

if res.status_code == 200:
    with open('.test', 'w') as fp:
        fp.write(res.text)



