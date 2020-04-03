"""
|               管道符表示对左右两边的表达式或的操作



"""
"""
1匹配0-100之间的数字

\d\d?|100




"""

import re
str = '01'
a = re.match('^[1-9]\d?$|^100$|^0$',str)
if a is not None:
    try:
        print('\033[1;32m匹配成功:',end='')
        print(a.group(),'\033[0m')
    except Exception as err:
        print(err)

else:
    print('\033[1;31m匹配失败\033[0m')


