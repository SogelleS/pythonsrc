def printLine(str,num):

    print(str*num)

def printLines(lines,str,num):
    """
    peint lines
    :param lines:line times
    :param str: str to print
    :param num: one line
    """
    i=0
    while i<lines:
        printLine(str,num)
        i+=1

printLines(5,'%',55)