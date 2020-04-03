import random
userin=int(input('stone 1 jiandao 2 bu 3:'))
comin=random.randint(1,3)

'''
 ((userin==1 and comin==2)
    or(userin==2 and comin==3)
    or(userin==3 and comin==1)):
'''
print('com use %d'%comin)

if userin==1:
    if userin==comin:
        print('try again')
    elif comin==2:
        print('you win')
    else:
        print('you loss')
if userin==2:
    if userin==comin:
        print('try again')
    elif comin==1:
        print('you loss')
    else:
        print('you win')

if userin==3:
    if userin==comin:
        print('try again')
    elif comin==1:
        print('you win')
    else:
        print('you loss')