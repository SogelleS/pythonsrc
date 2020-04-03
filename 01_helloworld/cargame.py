import py2exe
str1='0'
flag=0
str1=input(">")
while (str1.lower()!='quit'):
    #print(str1.lower())

    if(str1.lower()=='start'):

        if(flag==1):
            print('car already startd')
        else:
            print(">>>>>")
            flag=1

    elif(str1.lower()=='stop'):
        if(flag==0):
            print('car already stop')
        else:
            print('stoped')
            flag=0
    else:
        print(f"i cant understand: {str1}")
    str1=input(">")
print("bye")
