import requests,re,tqdm,os

url = 'https://onejav.com/'
prox = {
    'http':'http://127.0.0.1:1083',
    'https':'https://127.0.0.1:1083'
}

hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; '\
                  'Win64; x64) AppleWebKit/537.36 '\
                  '(KHTML, like Gecko) Chrome/80.0.3'\
                  '987.149 Safari/537.36'
}


def getdaymovnumber(num_str,page_maxnumber_str):
    text = gettext(num_str,page_maxnumber_str)
    res_url_list = re.findall('src=\"(https://pics\.dmm\.co\.jp/mono/movie/adult/.*\.jpg)\">', text)
    return len(res_url_list)+((page_maxnumber_str-1)*10)


def gettext(num_str,page):
    url_page = url + num_str + '?page=%s' % page
    #print(url_page)
    res = requests.get(url=url_page, headers=hd, proxies=prox)
    return res.text


def getdayphoto(days):

    text = gettext(days, '1')
    res_url_pagemun = re.findall('>(\d{1,2})</a></li>', text)
    temp_max = '1'
    if len(res_url_pagemun)==4:
        while True:
            temp_max = res_url_pagemun[-1]
            text = gettext(days,temp_max)
            res_url_pagemun = re.findall('page=(?P<page>\d{1,2})\">(?P=page)</a></li>', text)
            if temp_max>res_url_pagemun[-1]:
                break
    else:
        temp_max = res_url_pagemun[-1]


    # daymaxmov = getdaymovnumber(days,res_url_pagemun[-1])

    for i in range(1,int(temp_max)+1):
        flag = 0
        text = gettext(days, str(i))
        #print(text)

        res_url_list = re.findall('src=\"(https://pics\.dmm\.co\.jp/mono/movie/adult/.*\.jpg)\">', text)
        res_code_list = re.findall('<a href=\"/torrent/(.*)\">', text)
        res_torrent_list = re.findall('href=\"(/torrent/.*\.torrent)\" rel=\"',text)

        #print(i,res_url_list,sep='\t')
        #print(i,res_code_list,sep='\t')
        #print(i,res_torrent_list,sep='\t')
        days_in_filename = str(days).replace('/','-')

        for j in tqdm.tqdm(range(len(res_url_list)),ncols=65):
            if os.path.isfile('E:\\phtoto\\%s' % ('[%s]' % days_in_filename + res_code_list[j] + '.jpg')):
                flag = 1
                continue
            recv = requests.get(url=res_url_list[j], headers=hd, proxies=prox)
            with open('E:\\phtoto\\%s' % ('[%s]' % days_in_filename + res_code_list[j] + '.jpg',),'wb') as filep:
                filep.write(recv.content)

            full_torrent_down_link = url + res_torrent_list[j]
            recv = requests.get(url=full_torrent_down_link, headers=hd, proxies=prox)
            with open('E:\\phtoto\\%s' % ('[%s]' % days_in_filename + res_code_list[j] + '.torrent',),'wb') as filep:
                filep.write(recv.content)


if __name__ == '__main__':
    date = input('输入爬取日期(如2020/03/26):')
    getdayphoto(date)
    #getdaymovnumber()





