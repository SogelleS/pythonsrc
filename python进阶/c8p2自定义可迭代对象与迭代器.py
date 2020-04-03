#!/usr/bin/env python
# coding: utf-8

# ## 自定义的列表类型(自定义类)

# ![pt](https://github.com/SogelleS/PythonNotevookPhotos/blob/master/%E6%8D%95%E8%8E%B7.JPG?raw=true)

# ##### 需要有三个方法
# 1. 构造方法
# 2. 向对象中添加数据的方法
# 3. 迭代器方法  

# ##### 需要创建两个类  
# 1. 自定义类
# 2. 自定义迭代器类

# #####  实现效果

# In[2]:


for i in range(5):
    print(i,end=' ')


# #### 自定义类 

# In[18]:


class MyList(object):
    def __init__(self):
        self.data = []
        
        pass
    def __iter__(self):
        # 返回一个迭代器
        my_iter = MyIter(self.data)
        
        return my_iter
        
        pass
    def additem(self,thing):
        self.data.append(thing)
        print(self.data)
        pass
    


# #### 自定义类的迭代器类

# In[19]:


class MyIter(object):
    def __init__(self,mylist):
        self.list_len = len(mylist)
        self.list = mylist
        self.local_index = 0
        pass
    # def __iter__(self):
        # pass
    def __next__(self):
        # 判断是否越界 越界抛出异常
        if self.local_index < self.list_len:
            
            # 根据下标获取值
            data = self.list[self.local_index]
            
            # 下标位置加一
            self.local_index += 1
        else:
            raise StopIteration
            # 抛出停止迭代异常
        
        
        # 返回下标数据
        return data
        


# #####  添加元素

# In[20]:


mylist = MyList()
mylist.additem('1')
mylist.additem('2')
mylist.additem('3')
mylist.additem('4')
mylist.additem('5')


# In[22]:


for i in mylist:
    print(i, end=' ')


# In[ ]:





# In[ ]:




