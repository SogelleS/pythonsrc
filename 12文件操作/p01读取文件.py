# 文件操作的步骤
# 打开文件，读取修改文件，关闭文件

file = open('readme')

text = file.read()

# 一次性全部读取

print(text, end='')

file.close()


