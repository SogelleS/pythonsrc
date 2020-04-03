import requests

url = 'https://fanyi.baidu.com/sug'

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

data = {'kw': "弟弟"}

# 发送请求
res = requests.post(url, headers=hd, data=data)

# 接受数据
print(res.status_code)
# print(res.text)
print(res.json())

data = res.json()
print(data['data'][0]['k'])
# print(data['data'][0]['v'])
v = data['data'][0]['v']
v = v.split(';')[-2][1:]

print(v)



