def import_module1():
    from fibo import fib, fib2, my_var
    fib(500)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
    fib(100)  # 0 1 1 2 3 5 8 13 21 34 55 89
    print(my_var)  # dov
    # print(_var) NameError: name '_var' is not defined. Did you mean: 'my_var'?


# def import_module2():
#     from fibo import *
#     fib(500)


def import_module3():
    import fibo as fib
    fib.fib(500)


def import_module4():
    from fibo import fib as fibonacci
    fibonacci(500)


import_module1()
# import_module2()
import_module3()
import_module4()
