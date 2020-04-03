numbers=[1,2,3,4,5,600,7,8,9,100]
temp=numbers[0]
index=0
for index in range(9):
    if numbers[index]<numbers[index+1] and numbers[index+1]>temp:
        temp=numbers[index+1]
    elif numbers[index]>=numbers[index+1] and numbers[index] > temp:
        temp=numbers[index]

print(temp)