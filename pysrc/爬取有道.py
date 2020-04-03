import requests


def trans(word):

    url = 'https://fanyi.baidu.com/sug'
    hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    data = {'kw': word}
    res = requests.post(url, headers=hd, data=data)
    data = res.json()
    v = data['data'][0]['v']
    v = v.split(';')[-2][1:]
    return v


if __name__=='__main__':

    wd = input('enter to trans: ')
    print(trans(wd))


