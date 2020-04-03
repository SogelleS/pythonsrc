import requests

hd = {'User-Agent': 'Mozilla/73.0.1'}
try:
    r = requests.get('https://www.amazon.cn/gp/product/B07T7CW9ZR', headers=hd)
    print(r.status_code)
    print(r.request.headers)
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    pass

# 使用header伪装浏览器
# 测试失败
