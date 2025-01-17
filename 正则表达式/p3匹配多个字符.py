"""
*               前一个字符出现0次或者无限次
+               前一个字符出现1次或者无限次
？              0次或者1次要么要么有要么没有
{m}             前一个字符出现m次
{m,n}           前一个字符出现m次到n次


"""
# 练习
"""
1 找出字符串中第一个以大写字母开头的子字符串
bbsdAdwqq       [A-Z][a-z]*     Adqqd
1 找出字符串中第一个以大写字母开头的含有4各字符的子字符串
bbsaRetss       [A-Z][a-z]{3}   Rets

2 匹配一个变量名是否有效
dad22w          [a-zA-Z_]+\w*   dad22w

3 匹配出0-99之间的数字
ww331eq         \d\d? or \d?\d          33  1
3 匹配数字
ww331ee532q     \d\d*                   331 532

4 寻找连续4位的数字
ad672asd2314sd22da  \d{4}               2314
4 不是以4，7结尾的手机号（11位）
xxxxxxx         \d{10}[1235689]
xxxxxxx         \d{10}[0-35-68-9]

5 匹配8-20位的密码可以是大小写数字下划线
xxxxxxx         [a-zA-Z0-9_]{8,20}
                \w{8,20}

练习 匹配163的邮箱@之前有4-20位
hello@163.com   \w{1}[a-zA-Z0-9]{3,19}@163\.com

# .有特殊含义需要换成\.

"""