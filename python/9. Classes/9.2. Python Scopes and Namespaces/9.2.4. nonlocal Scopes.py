# https://www.youtube.com/watch?v=WYZrLtFNDVI
a = 35


def outer():
    x = 25

    def inner():
        nonlocal x
        x = 30

    inner()
    print(x)  # 30


# we want to print x but if we put global instead of nonlocal it will create x in the global scope
outer()