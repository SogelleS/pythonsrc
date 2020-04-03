def pF(maxlim):


    if (maxlim==1 or maxlim==2):

        #print(1,end=' ')
        return 1
    else:
        #print(pF(maxlim - 1)+pF(maxlim-2), end=' ')
        return pF(maxlim-1)+pF(maxlim-2)





for i in range(31)[1::]:
    print('%-7d'%pF(i),end=' ')
    if i%8==0:
        print()