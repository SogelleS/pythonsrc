poem=['abc','abcd','abcde','abcdef','abcdefg']

for str in poem:
    print('|%s|'%str.center(20,'*'))    #可以使用中文空格

print("#"*30)

for str in poem:
    print('|%s|'%str.ljust(20,'*'))

print("#"*30)

for str in poem:
    print('|%s|'%str.rjust(20,'*'))
