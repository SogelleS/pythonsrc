a1 = 1
a2 = 1
i = 1
index = 0


def pf(mix):

    global a1
    global a2
    global i
    global index

    if i == 1 or i == 2:
        print('%-10d' % 1, end=' ')

    else:
        n = a1 + a2
        a1 = a2
        a2 = n
        print('%-10d' % n, end=' ')

    index += 1
    i += 1

    if index == 4:
        print()
        index = 0

    if i == mix+1:
        return 0
    else:
        pf(mix)


pf(12)





