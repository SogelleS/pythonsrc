import re,requests,time


class Get(object):
    def __init__(self,url,usecode='utf-8',regx=''):
        self.url = url
        self.regx = regx
        self.usecode = usecode


    def useRegxGet(self):
        res = self.getUrlText()
        resu = re.findall(self.regx,res)
        return resu

    def getUrlText(self):
        hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; '\
                            'Win64; x64) AppleWebKit/537.36 '\
                            '(KHTML, like Gecko) Chrome/80.0.3'\
                            '987.149 Safari/537.36'}
        res = requests.get(url=self.url,headers=hd)
        res.encoding=self.usecode
        return res.text



if __name__ == '__main__':
    # a = Get(url='http://www.lwgod.xyz/forum-292-1.html',\
    #         regx='\">(【.*】)<',\
    #         usecode='gbk')
    while True:
        num = input('enter page num:')
        url = 'https://www.btba.cc/type/%E7%94%B5%E5%BD%B1.html?page=' + num
        a = Get(url=url,\
                regx='\"(.*?)\">(.*?)</a><b>',)
        res = a.useRegxGet()
        for i in range(len(res)):
            print(res[i])



