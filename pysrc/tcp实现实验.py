nlist = []
templist = -1
flag = 0

for i in [1,3,2,4,5]:
    if i == 1:
        nlist.append(i)
        bef = 1

    else:
        if i == bef + 1:
            nlist.append(i)
            bef = i
            if flag == 1:
                nlist.append(templist)
                bef = templist
                flag = 0
            
        elif i > bef + 1:
            templist = i
            flag = 1
    
            
            
print(nlist)
