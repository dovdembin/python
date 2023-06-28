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
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)
            # if a raise is happening we need to handle here

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
