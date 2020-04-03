a=45
print('%06d'%a)
print('%16d'%a)
print('%016d'%a)
print('%-6d'%a)

''''
from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.01)
    pass
'''

scale=0.25
print('nam is %.2f%%'%(scale*100))