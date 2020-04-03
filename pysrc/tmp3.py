'''
      汉诺塔问题
         +          +          +
         +          +          +
         #          +          +
        ###         +          +
       #####        +          +
      #######       +          +
     #########      +          +
=========A==========B==========C=========
'''


i = 0
check = 1


def tower2tower(stower, ttower, elsetower, towernum):
    global i
    global check
    if towernum == 1:
        i += 1
        print('(%-3d) %s ---> %s' % (i, stower, ttower))
    else:
        tower2tower(stower, elsetower, ttower, towernum-1)
        tower2tower(stower, ttower, elsetower, 1)           # print('%s ---> %s' % (stower, ttower))
        tower2tower(elsetower, ttower, stower, towernum-1)
    if check == towernum:
        print('*'*50)
        check += 1


num = int(input('塔有几层？ ：'))
print('全部从A移动到C的过程：')
tower2tower('A', 'C', 'B', num)

