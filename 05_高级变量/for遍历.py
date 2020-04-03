nameList=['zhang','li','wang','zhao']

for name in nameList:
    for char in name:
        print(char,end=' ')

    print()

i=0
for i in range(100):
    print('%-3d'%(i+1),end=' ')
    if i%10==9:
        print()