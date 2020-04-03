poem=['abc','abcd','abcde','abcdef','abcdefg']

i=0
for str in poem:
    poem[i]=str.rjust(20)
    i+=1

#print(poem)

print(poem[0].strip())

#poem[0].lstrip()左删除
#poem[0].rstrip()右删除