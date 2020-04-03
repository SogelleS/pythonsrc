"""

(?P<name>.....)
在一个分组中开始的位置写?P<name>表示将这个分组命名为name
使用时用 (?P=neme) 表示 括号不能少


"""

"""

1使用别名匹配
<html><h1>test</h1></html>

regx    <(?P<n1>[a-zA-Z0-9]+)><(?P<n2>[a-zA-Z0-9]+)>(.*)<(/(?Pn2))><(/(?Pn1))>


"""

import re


def metch(regx, str, num=0):
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

    metch('<(?P<name1>[a-zA-Z0-9]+)><(?P<name2>[a-zA-Z0-9]+)>(.*)<(/(?P=name2))><(/(?P=name1))>',\
          str2)


