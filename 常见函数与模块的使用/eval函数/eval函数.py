print(eval('1 + 1'))
# eval 可以将字符串变成一个有效的表达式

print(eval("'#'*50"))

str = input('计算器：')

print(eval(input('计算器：')))

# 不要直接调用input 会产生任意代码执行漏洞

