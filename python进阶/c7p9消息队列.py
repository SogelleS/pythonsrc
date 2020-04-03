"""
可以使用multiprocessing中的queue实现进程之间的
数据传输Queue本身是一个消息队列程序

队列是个特殊的结构从一端放数据从另一端取数据



"""
import multiprocessing as mulp

'''
创建队列(指定长度)
放入值
取出值

'''

# 创建队列(指定长度)
que = mulp.Queue(5)

# 放入值
# 可以放数字类型,字符串,列表,字典,元组
que.put(10)
que.put('hello')
que.put([1,2,3,4])
que.put({'a':'aaa','b':'bbb'})
que.put((5,6,7,8))

# que.put(12)
# 超出上限5放入第6个数据后队列会进入堵塞状态
# 等待队列取出值后再放入新值
# que.put_nowait(14)
# 使用put_nowait不会造成堵塞会直接报错
# 取出值
for i in range(5):
    print(que.get())
    print('---'*20)

# print(que.get())
# 队列空了后再取值也会进入堵塞
# print(que.get_nowait())
# 队列空了会直接报错

