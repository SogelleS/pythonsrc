"""
\num        引用分组num匹配到的字符串(反斜杠)
            \1引用第一组数据在这里相当于html
            注意在字符串中要用\\表示表达式中的\





"""
"""
1 匹配    <html>test</html>

regx           <[a-zA-Z0-9]+>.*<[a-zA-Z0-9]+>
        
        不能检测两个尖括号内内容是否一致
        <([a-zA-Z0-9]+)>.*</\1>
        \1引用第一组数据在这里相当于html
        注意在字符串中要用\\表示表达式中的\
        <([a-zA-Z0-9]+)>(.*)</\\1>
        
2 匹配        <html><h1>test</h1></html>

regx          <([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)</\2></\1>
              <([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)</\2></\1>             

        

"""
import re


def metch(regx,str,num=0):
    a = re.match(regx, str)
    if a is not None:

        print('\033[1;32m%s匹配成功:' % str, end='')
        print(a.group())
        print('提取子字符串:', a.group(num))
        print('\033[0m',end='')
        print('#'*60)

    else:
        print('\033[1;31m%s匹配失败\033[0m' % str)


if __name__ == '__main__':

    str1 = '<html>test</html>'
    str2 = '<html><h1>test</h1></html>'

    metch('<([a-zA-Z0-9]+)>.*</\\1>', str1, num=0)
    metch('<([a-zA-Z0-9]+)>.*</\\1>', str1, num=1)
    metch('<([a-zA-Z0-9]+)>(.*)</\\1>', str1, num=2)

    metch('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)<(/\\2)><(/\\1)>',\
          str2, num=0)
    # metch('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)<(/\\2)><(/\\1)>', \
    #       str2, num=1)
    # metch('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)<(/\\2)><(/\\1)>', \
    #       str2, num=2)
    # metch('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)<(/\\2)><(/\\1)>', \
    #       str2, num=3)
    # metch('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)<(/\\2)><(/\\1)>', \
    #       str2, num=4)
    # metch('<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>(.*)<(/\\2)><(/\\1)>', \
    #       str2, num=5)



