# https://www.youtube.com/watch?v=IEEhzQoKtQU&t=1s
import threading
import time

start = time.perf_counter()


def do_something(second):
    print(f'Sleeping {second} second(s)...')
    time.sleep(second)
    print('Done Sleeping')


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
