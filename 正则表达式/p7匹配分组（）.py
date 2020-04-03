"""
()          将小括号里的字符作为一个整体（分组）
.group(XX) 获取正则里第XX个分组里的信息



"""
"""
1 匹配126.163.qq的邮箱
\w{4,20}@(163|126|qq)\.com
2 提取座机号码的区号和座机号
eg      010-12345678      0321-1234567
(\d{3}|\d{4})-(\d{8}|\d{7})
\d{3,4}-\d{7,8}     这个没有分组所以不能使用.group提取分组信息

"""
import re


def metch(regx,str,num=0):
    a = re.match(regx, str)
    if a is not None:

        print('\033[1;32m%s匹配成功:' % str, end='')
        print(a.group())
        print('提取子字符串:', a.group(num))
        # 获取正则里第几个分组里的信息
        print('\033[0m',end='')
        print('#'*60)

    else:
        print('\033[1;31m%s匹配失败\033[0m' % str)


if __name__ == '__main__':

    str1 = 'adojo@qq.com'
    str2 = '0105-3333333'

    metch('\w{4,20}@(163|126|qq)\.com',str1,num=1)

    metch('(\d{3}|\d{4})-(\d{8}|\d{7})',\
          str2,num=2)

    metch('\d{3,4}-\d{7,8}',str2,num=0)



