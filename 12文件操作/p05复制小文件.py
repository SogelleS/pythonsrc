sfile = open('readme')
tfile = open('readme2', 'w')

text = sfile.read()
tfile.write(text)


# while True:
#
#     line = sfile.readline()
#     if not line:
#         break
#     else:
#         tfile.writelines(line)


sfile.close()
tfile.close()

