def demo(num,list):

    print('+'*50)
    num+=num

    list+=list          #与list.extend(list)

    #列表使用+=不会像数字那样重新引用
    #实际上是对列表使用了extend方法

    #list=list+list
    #这是列表的重新引用

    print(num,list)
    print('+' * 50)


gl_num,gl_list=9,[1,2,3]
demo(gl_num,gl_list)

print(gl_num,gl_list)