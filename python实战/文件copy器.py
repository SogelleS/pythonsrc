import os
import shutil

while True:
    s_path = input('enter a s_path:')
    if (not os.path.isdir(s_path)) and (not os.path.isfile(s_path)):
        print('try again')
        continue
    else:
        break
ch = 0
while True:
    t_path = input('enter a t_path')
    if os.path.isdir(t_path):
        print('\033[31mt_path 已经存在了\033[0m')
        ch = input('1 覆盖,2 放弃,3 重新输入t_path')
        if ch == 1:
            shutil.rmtree(t_path)
            break
        elif ch == 2:
            break
        elif ch == 3:
            continue
        else:
            print('try again')
            continue
    else:
        break

if ch == 2:
    exit(0)

os.mkdir(t_path)
shutil.copy(s_path,t_path)
print('done')

