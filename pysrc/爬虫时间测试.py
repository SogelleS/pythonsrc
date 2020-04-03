import requests
import time
from tqdm import tqdm

url = 'http://www.baidu.com'

start_time=time.time()

for i in tqdm(range(0, 999)):
    try:
        requests.get(url)
    except Exception as err:
        print('err')

end_time=time.time()

print('爬取[%s]1000次用了 %.3f 秒' % (url, (end_time - start_time)))
