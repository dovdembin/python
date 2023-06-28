# https://www.youtube.com/watch?v=IT8RYokUvvQ
# Multiprocessing in Python - Advanced Python 17 - Programming Tutorial

from multiprocessing import Pool


def cube(number):
    return number * number * number


if __name__ == '__main__':
    numbers = range(10)
    pool = Pool()

    # map, apply, join, close
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0]) this unclear
    pool.close()
    pool.join()

    print(result)


