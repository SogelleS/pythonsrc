import requests

r = requests.head('http://baidu.com')
print(r.headers)

pload = {'key1': 'val1', 'key2': 'val2'}
r2 = requests.post('http://httpbin.org/post', data=pload)
r3 = requests.post('http://httpbin.org/post', data='abcd')


print(r2.text)
print(r3.text)









