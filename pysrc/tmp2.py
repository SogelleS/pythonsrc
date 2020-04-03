a1 = 1
a2 = 1
i = 1
index = 0

for temp in range(1, 20):
    if temp == 1 or temp == 2:
        print('%-10d' % 1, end=' ')
    else:
        n = a1 + a2
        a1 = a2
        a2 = n
        print('%-10d' % n, end=' ')
    index += 1
    if index == 4:
        print()
        index = 0


