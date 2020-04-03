"""

1判断是否满了
.full()方法

2判断是否空了
.empty()方法

3取出队列中目前存在的消息个数
.qsize()返回个数


"""
import multiprocessing as mulp
# 创建队列
qu = mulp.Queue(3)

qu.put(1)
qu.put(2)
qu.put(3)


# 1判断是否满了
a = qu.full()
print(a)
# >>True


# 3取出队列中目前存在的消息个数
qu.get()
b = qu.qsize()
print(b)
# >>2


# 2判断是否空了
qu.get()
qu.get()
c = qu.empty()
print(c)





