def demo1(*args,**kwargs):

    print(args)
    print(kwargs)


num=(1,2,3)
dic={'1':1,'2':2,'3':3}

dic1={1:1, 2:2, 3:3}

demo1(num,dic)

#((1, 2, 3), {1: 1, 2: 2, 3: 3})


demo1(*num,**dic)
demo1(**dic1)
#TypeError: demo1() keywords must be strings



