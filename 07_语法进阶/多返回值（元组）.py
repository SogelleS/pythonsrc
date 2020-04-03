def measure1():
    '''测量温度和湿度'''

    print('statring.....')
    temp = 30
    wetness = 50

    print('end')

    #return (temp,wetness)       #打包返回值，小括号可以省略
    return temp,wetness

def measure2():
    '''测量温度和湿度'''

    print('statring.....')
    temp = 30
    wetness = 50
    re={'temp':temp, 'wet':wetness}
    print('end')

    return re
    #返回一个字典


re=measure1()
print(re)
print(measure2())

#需要单独处理温度或湿度(麻烦容易出错)

print(re[0])
print(re[1])

#可以使用多个全局变量一次性接收

gl_temp,gl_wet=measure1()
print(gl_temp)
print(gl_wet)