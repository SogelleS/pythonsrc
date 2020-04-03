import requests


def getHtmlText(url):

    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except Exception as perr:
        return perr


if __name__ == '__main__':
    print(getHtmlText('www.baidu.com'))
    print(getHtmlText('http://www.baidu.com'))
    # print(getHtmlText('https://www.google.com'))


