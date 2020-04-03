"""
与线程守护类似
当主进程结束时子进程也会结束

设置pa守护主进程
pa.daemon = True

设置强制杀死子进程pa
pa.terminate()

"""

import multiprocessing,time

def work():

    for i in range(10):
        print('<----------work--------->')
        time.sleep(0.5)


if __name__ == '__main__':

    pa = multiprocessing.Process(target=work)
    pa.daemon = True
    pa.start()
    time.sleep(2)
    print('main process is killed')

    pa.terminate()

    exit(0)
