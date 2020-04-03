sfile = open('readme')
tfile = open('readme2', 'w')


while True:

    line = sfile.readline()
    if not line:
        break
    else:
        tfile.writelines(line)


sfile.close()
tfile.close()

