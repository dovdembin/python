# https://www.youtube.com/watch?v=vbtxtvuCFRM
# Threading vs Multiprocessing in Python - Advanced Python 15 - Programming Tutorial

from threading import Thread
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == '__main__':
    threads = []
    num_threads = 10

    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    # start
    for t in threads:
        t.start()

    # join
    for t in threads:
        t.join()

    print('end main')
