# https://www.youtube.com/watch?v=IEEhzQoKtQU&t=1s
import concurrent.futures
import time


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


if __name__ == '__main__':

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)

        print(f1.result())
        print(f2.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
