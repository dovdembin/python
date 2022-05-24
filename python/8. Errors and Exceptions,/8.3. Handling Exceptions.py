import sys


def try_except():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try agdain...")
        except (RuntimeError, TypeError, NameError):
            print("Oops")


def class_in_an_except():
    class B(Exception):
        pass

    class C(B):
        pass

    class D(C):
        pass

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")


def base_exception():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except BaseException as err:  # BaseException as a wildcard
        # if exception name is omitted must retrieve from sys.exc_info()[1].
        print(f"Unexpected {err=}, {type(err)=}")
        raise


def try_except_else(arg):
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


def raise_exception():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)  # __str__ allows args to be printed directly,
        # but may be overridden in exception subclasses
        x, y = inst.args  # unpack args from (instance.args)
        print('x =', x)
        print('y =', y)


try_except()
class_in_an_except()
base_exception()
try_except_else("out.txtttt")  # should be out.txt
raise_exception()


def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
