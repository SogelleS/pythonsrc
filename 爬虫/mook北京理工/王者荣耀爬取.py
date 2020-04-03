import requests
import os
import threading
import shutil
import tqdm

userHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

def getjpg(hero_num,file_path):

    baseurl = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/'

    hero_num = str(hero_num)
    herourl = baseurl + '/' + hero_num + '/' + hero_num +'.jpg'
    web = requests.get(url=herourl,headers=userHeaders)
    if web.status_code != 200 :
        return

    else:
        with open(file_path + hero_num + '.jpg','wb') as file:
            file.write(web.content)
        with open('test.txt','a') as tfile:
            tfile.write(hero_num+'\n')


def puth(num,path):
    for i in range(num,num+101):
        getjpg(i,path)


if __name__ == '__main__':

    if os.path.exists('E:\\pythonsrc\\hero'):
        shutil.rmtree('E:\\pythonsrc\\hero')

    os.mkdir('E:\\pythonsrc\\hero')

    for i in range(100,600,100):
        th = threading.Thread(target=puth,args=(i,'E:\\pythonsrc\\hero\\'))
        th.start()



    # for i in tqdm.tqdm(range(105,200)):
    #     getjpg(i,'E:\\pythonsrc\\hero\\')
    # for i in range(312,313):
    #     getjpg(i,'E:\\pythonsrc\\hero\\')
    # for i in tqdm.tqdm(range(501,530)):
    #     getjpg(i,'E:\\pythonsrc\\hero\\')
    # for i in range(500,550):
    #     getjpg(i,'E:\\pythonsrc\\hero\\')
    # getjpg(507,'E:\\pythonsrc\\')


