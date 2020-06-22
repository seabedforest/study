"""
练习2 ： 有两个线程同时运行，一个线程负责打印 1---52 52个数字
另一个线程打印 A-Z 26个字母
要求打印的的顺序是12A34B56C....5152Z
使用同步互斥方法进行打印顺序的管控
"""
from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()


def play_num():
    for i in range(1, 53, 2):
        lock1.acquire()
        print(i)
        print(i + 1)
        lock2.release()


def play_word():
    for w in range(65, 91):
        lock2.acquire()
        print(chr(w))
        lock1.release()


t1 = Thread(target=play_num)
t2 = Thread(target=play_word)

lock2.acquire()
t1.start()
t2.start()

t1.join()
t2.join()
