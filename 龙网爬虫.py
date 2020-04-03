import time,requests,re,threading,tqdm

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
baseurl = 'http://www.lwgod.xyz/'


def getlwgodpage(page_url,page_num):

    res = requests.get(url=page_url,headers=hd)
    res.encoding = 'gbk'
    getlist2 = re.findall('<a href=\"(thread.*.html)\" onclick=\"atarget\(this\)\" class=\".*?\">(.*)</a>', res.text)


    # for tqdmi in tqdm.tqdm(range(len(getlist2)),ncols=60):
    for tqdmi in range(len(getlist2)):
        murl,mname = getlist2[tqdmi]
        murl = baseurl + murl
        # 添加根目录
        s_page = requests.get(murl,headers=hd)
        s_page.encoding = 'gbk'
        meg = re.search('(magnet:.*)<br />',s_page.text)
        #lock1.acquire()
        #fp = open('lwmug.txt', 'a', encoding='utf-8')
        if meg == None:
            try:
                meg =re.search('\"(plugin.*)\"',s_page.text)
                meg = baseurl + meg.group(1)
                #print('p%3d ' % page_num,'%2d' % (tqdmi+1),' '+ meg + '\n',mname,'\n')
                print(meg + '\n', mname, '\n',sep='')

                #fp.write(meg + '\n' + mname + '\n\n')
            except:
                continue

        else:
            #print('p%3d ' % page_num,'%2d' % (tqdmi+1),' ' + meg.group(1) + '\n',mname,'\n')
            print(meg.group(1) + '\n', mname, '\n',sep='')
            #fp.write(meg.group(1) +'\n' + mname + '\n\n')
        #fp.close()
        #lock1.release()


def getPageNumUrl(pagenum):
    baseurl = 'http://www.lwgod.xyz/forum-18-1.html'
    pagenum = str(pagenum)
    turl = re.sub('-\d\.html','-'+pagenum+'.html',baseurl)

    return turl

def thget(num):
    getlwgodpage(getPageNumUrl(num), num)


if __name__ == "__main__":
    page1 = 'http://www.lwgod.xyz/forum-18-1.html'
    # lock1 = threading.Lock()
    num = 1
    for i in range(num):
        t = threading.Thread(target=thget,args=(i,))
        t.start()


    #getlwgodpage(getPageNumUrl(num),num)



