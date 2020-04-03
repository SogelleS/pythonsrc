def mul_tab():
    i=1

    '''
    while i<=9:
        j=i
        while j<=9:
            print('%dx%d=%-2d'%(i,j,i*j),end='    ')
            j+=1
        print('')
        i+=1
    '''

    while i<=9:
        j=1
        while j<=i:
            print('%dx%d=%-2d' % (j, i, i * j), end='    ')
            j+=1
        print('')
        i+=1

