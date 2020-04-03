def demo1(num_list):
    print('+'*50)
    #num_list=[1,1,1,1]
    num_list.append(9)      #方法是对原有内存的修改，赋值是引用
    print(num_list)

    print('+' * 50)

gl_list=[1,2,3,4]
demo1(gl_list)

print(gl_list)
