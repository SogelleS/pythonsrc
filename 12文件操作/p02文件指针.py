file = open('readme')
text = file.read()
print(text, end='')
print(len(text))

# 运行完后文件指针位于文件末尾
# 再次运行不能读取内容

print('*'*50)
text = file.read()
print(text,end='')
print(len(text),end='')
file.close()

