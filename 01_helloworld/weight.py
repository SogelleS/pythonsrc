wei=int(input('you weight'))
ch=input('(L)or(k):')

if (ch[0]=='l' or ch[0]=='L'):
    print('you are %.2f'%(wei*0.45))
elif (ch[0]=='k' or ch[0]=='K'):
    print('you are %.2f'%(wei/0.45))
else:
    print('error')
