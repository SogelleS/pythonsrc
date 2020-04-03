file = open('readme', 'r')

print(len(''))

while True:
    line = file.readline()
    if not line or line == '\n':
        break
    print(line,end='')

    print('+'*50)



file.close()

