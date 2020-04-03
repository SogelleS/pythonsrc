'''
对英文文章统计出现次数最高的10个单词
以及次数

'''

import re
txt = open('engtext.txt').read()

print(re.split('\w',txt))


