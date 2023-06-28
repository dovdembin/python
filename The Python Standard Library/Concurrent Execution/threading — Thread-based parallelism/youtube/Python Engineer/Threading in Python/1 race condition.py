# https://www.youtube.com/watch?v=usyg5vbni34
# Threading in Python - Advanced Python 16 - Programming Tutorial

from threading import Thread
import time

database_value = 0


def increase():
    global database_value

    local_copy = database_value

    # processing
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy


if __name__ == '__main__':
    print('start value', database_value)

    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)

    print('end main')
