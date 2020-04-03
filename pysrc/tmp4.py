def tower2tower(stower, ttower, elsetower, towernum):
    if towernum == 1:
        print('%s ---> %s' % (stower, ttower))
    else:
        tower2tower(stower, elsetower, ttower, towernum-1)
        print('%s ---> %s' % (stower, ttower))
        tower2tower(elsetower, ttower, stower, towernum-1)
tower2tower('A', 'C', 'B', 10)
