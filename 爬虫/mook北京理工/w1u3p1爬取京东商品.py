import requests

try:
    r = requests.get('https://item.jd.com/100011513372.html')
    r.raise_for_status()

    # r.encoding = r.apparent_encoding
    # r.encoding = 'gbk'

    print(r.text[:1000])
    # 大文件切片显示

except Exception as err:
    print(err)


