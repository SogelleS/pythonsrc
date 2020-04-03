import requests

keyword = {'wd': 'python'}

try:
    r = requests.get('http://www.baidu.com', params=keyword)
    print(r.url)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))

except:
    pass





