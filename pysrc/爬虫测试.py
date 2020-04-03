import requests
import chardet

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

url = 'https://www.laod.cn/'
url2 = 'http://www.lwgod.xyz/'

test1 = requests.get(url,headers=hd)
test2 = requests.get(url2,headers=hd)
print(test2.encoding)
print(test2.apparent_encoding)
test2.encoding='gbk'
#test3 = test2.text.encode('utf-8')
#test3 = test3.decode('utf-8')

# with open('demo.txt','w',encoding='utf-8') as file:
#     file.write(test1.text)
with open('demo.tpad','w',encoding='utf-8') as file:
    file.write(test2.text)
with open('demo.tpad','rb') as file2:
    data = file2.read()
    print(chardet.detect(data))


