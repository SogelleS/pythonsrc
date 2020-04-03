nlist = []
templist = []
flag = 0

for i in [(1,'a'),(3,'c'),(4,'d'),(2,'b'),(5,'e')]:
    if i[0] == 1:
        nlist.append(i)
        bef = i

    else:
        if i[0] == bef[0] + 1:
            nlist.append(i)
            bef = i
            if flag >= 1:
                nlist.append(tuple([bef[0]+1,[x for x in templist if x[0]==bef[0]+1]]))
                bef = templist[0]
                flag -= 1
            
        elif i[0] > bef[0] + 1:
            templist.append(i)
            flag += 1
    
            
            
print(nlist)
