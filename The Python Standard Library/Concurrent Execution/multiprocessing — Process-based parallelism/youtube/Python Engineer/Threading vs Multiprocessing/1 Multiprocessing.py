# https://www.youtube.com/watch?v=IT8RYokUvvQ
# Multiprocessing in Python - Advanced Python 17 - Programming Tutorial

from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == '__main__':
    processes = []
    num_process = os.cpu_count()

    for i in range(num_process):
        process = Process(target=square_numbers)
        processes.append(process)

    # start
    for process in processes:
        process.start()

    # join
    for process in processes:
        process.join()

    print('end main')
