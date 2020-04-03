"""
1 获取文件夹名字

2 创建新的文件夹

3 读取源文件夹内文件
使用 os.listdir() 获取文件夹内文件名

4 复制源文件夹到新文件夹中去
采用进程池异步方式

注意如果在子进程中发生了异常终端不会输出

5 实现进度查看
创建进程间队列


"""


def copy_file(file_name,so_folder,target_folder,q):

    #print('%s------>%s' % (so_folder+'/'+file_name,\
                           #target_folder))

    sof = open(so_folder+'/'+file_name,'rb')
    tarf = open(target_folder+'/'+file_name,'wb')
    tarf.write(sof.read())
    sof.close()
    tarf.close()
    q.put(file_name)



import os,multiprocessing

if __name__ == '__main__':

    # 获取源路径与创建目标文件夹
    so_folder = input('target folder path :')
    if '/' not in so_folder:
        so_folder = so_folder.replace('\\','/')
    #print(so_folder)
    file_list = os.listdir(so_folder)
    target_folder = so_folder + '-复件'

    # 抛出异常是文件夹不用手动删除
    try:
        os.mkdir(target_folder)
    except:
        pass

    # 创建进程池
    po = multiprocessing.Pool(5)

    # 创建队列
    q = multiprocessing.Manager().Queue()

    # 向进程池添加任务
    for file_name in file_list:
        po.apply_async(copy_file,(file_name,\
                                  so_folder,\
                                  target_folder,\
                                  q))

    po.close()
    # po.join()
    i=len(file_list)
    while i > 0:

        file_name = q.get()
        # print(file_name)

        i-=1
        print('\r进度(%d/%d)' % (len(file_list)-i,\
                             len(file_list)),end='')

    print()


