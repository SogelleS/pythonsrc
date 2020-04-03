def sumNumber(num):

    #print(num)
    if num == 1:
        return 1
    else:
        return (sumNumber(num-1)+num)

print(sumNumber(100))