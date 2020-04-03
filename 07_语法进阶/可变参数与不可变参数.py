def demo(num,num_list):

    num=100
    #不会修改外部变量，不论可变与不可变类型
    num_list=[1,2,3]

    print('='*40)
    print(num)
    print(num_list)
    print('='*40)

gl_num=99
gl_list=[4,5,6]

demo(gl_num,gl_list)
print(gl_num)
print(gl_list)