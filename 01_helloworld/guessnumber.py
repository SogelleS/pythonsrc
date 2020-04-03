i=0;
flag=0;
#while (i<3):
while (i<3 and flag==0):
    num=int(input('you number '))
    if (num==9):
        print('good')
        flag=1;
        #break
    i+=1
if (flag==1):
    print('done')
