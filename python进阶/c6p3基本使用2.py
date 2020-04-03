import time
import threading


def sing():
    print('sing')
    time.sleep(0.5)


def dance():
    print('dance')
    time.sleep(0.5)


if __name__ == '__main__':
    for i in range(5):
        A = threading.Thread(target=sing)
        B = threading.Thread(target=dance)
        A.start()
        B.start()



