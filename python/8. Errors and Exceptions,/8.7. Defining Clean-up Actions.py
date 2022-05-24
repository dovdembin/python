def no_raise():
    for i in range(0, 3):
        try:
            raise KeyboardInterrupt
        finally:
            print('Goodbye, world!')
            break  # because of break no rais could be "continue or return " too


def bool_return():
    try:
        return True
    finally:
        return False


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


no_raise()
print(bool_return())  # False

divide(2, 1)
divide(2, 0)
divide("2", "1")
