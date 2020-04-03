import requests


def getname():

    url = 'https://www.lmonkey.com/my/classrooms'
    hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
          'cookie': 'UM_distinctid=170f28035fd2b-04eef54984b8fb-f313f6d-1fa400-170f28035fe86a; accessId=ad8e1ca0-2091-11ea-af9d-6523a0f144a7; Hm_lvt_676e52e2eddd764819cab505b21e9ee8=1584616454,1584673020; qimo_seosource_ad8e1ca0-2091-11ea-af9d-6523a0f144a7=%E7%99%BE%E5%BA%A6%E6%90%9C%E7%B4%A2; qimo_seokeywords_ad8e1ca0-2091-11ea-af9d-6523a0f144a7=; href=https%3A%2F%2Fwww.lmonkey.com%2F; CNZZDATA1277679765=1547559497-1584613145-%7C1584673417; XSRF-TOKEN=eyJpdiI6IlNBQVpSUXBsWmx1ak1wVUtTcnZwQXc9PSIsInZhbHVlIjoieDZNVnZcL1o2cEpZdjN2dXlNUnlPM2R2OWhRMXJFdTVJTUxSUXY4T3Z5cE5sQlo0eWpoWGlib0g4Vm40ZEllTGciLCJtYWMiOiJhZjUyNzNhMDI1YmI4YmM2ZTJmYjEzZDkzNDU3N2I5MjI5MTkzMjViNTQyNDE5YzVhN2U3ZjcxNDc1MmVhZDFjIn0%3D; _session=eyJpdiI6InVTRHJlYjRNQTZYZHAxbkptdXA2Snc9PSIsInZhbHVlIjoicXVkXC9GeHVoVlVSeU1xc2NNcUtvamNzWWFLRWNWVUVtR1FTdUgySHVabFEzc2FZMzRKWlh0OHU5Wlc1ZXlaeEMiLCJtYWMiOiI2MDlkMDVlZTFmYzM3NmQ3MzdiMmUyYmI4NzQzMzJhYzkwZDlmOGFlOTliMTgxOTkxZjZiMjBkZjViZTNjZWU4In0%3D; Hm_lpvt_676e52e2eddd764819cab505b21e9ee8=1584673717; pageViewNum=13'}

    res = requests.get(url, headers=hd)
    if res.status_code == 200:
        for ch in res.text:
            print(ch,end='')

    return res.status_code


if __name__ == '__main__':

    print(getname())
