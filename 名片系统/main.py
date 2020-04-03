#! C:\Users\Xen\AppData\Local\Programs\Python\Python38\python.exe

import main_tool

'''
choice = main_tool.puthelp()

while choice not in [0,1,2,3]:
    print('Error use 0,1,2,3')
    choice = main_tool.puthelp()

while (choice != 0):
    print("you choose",choice)
    if choice==1:


    elif choice==2:


    else:


    choice=main_tool.puthelp()
'''

#第二种架构

while True:
    choice = main_tool.puthelp()
    #print('you choice:',choice)
    if choice==0:
        break
    elif choice==1:         #todo 新增名片
        main_tool.addcard()

    elif choice==2:         #todo 显示全部

        main_tool.showall()
    elif choice==3:         #todo 查询名片

        main_tool.serchcard()
    else:
        print('Error use 0,1,2,3')
        continue

print('DONE!!!')