# https://www.youtube.com/watch?v=usyg5vbni34
# Threading in Python - Advanced Python 16 - Programming Tutorial

from threading import Thread, Lock, current_thread
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()
        # processing..
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True # deamon thread die when the main thread die
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print('end main')
