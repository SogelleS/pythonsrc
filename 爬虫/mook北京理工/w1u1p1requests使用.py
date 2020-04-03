import requests

r = requests.get('https://www.baidu.com')
print(r.apparent_encoding)
print(r.text)
r.encoding = 'utf-8'
# 如果httphader没有编码形式，默认编码为iso-8859-1
# apparent_encoding是根据分析获取的网页编码
print(r.text)