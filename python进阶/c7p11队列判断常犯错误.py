"""
填入数据后使用.empty方法判断会失误

解决方法
sleep一会就解决了

"""
import multiprocessing as mulp
import time

a = mulp.Queue(3)

# 填入相同的三个值
for i in range(3):
    a.put(i, block=False)

#time.sleep(0.001)

isEmpty = a.empty()
print(isEmpty)
