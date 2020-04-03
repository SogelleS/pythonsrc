import requests
import os

url = 'https://cdn.laod.wang/wp-content/uploads/2018/07/dns.jpg'
root = 'C:\\Users\\Xen\\Pictures'

r = requests.get(url)

f = open('E:\\pythonsrc', 'wb')
f.write(r.content)
f.close()

