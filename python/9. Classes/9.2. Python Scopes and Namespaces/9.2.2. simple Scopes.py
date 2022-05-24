# https://www.youtube.com/watch?v=WYZrLtFNDVI
a = 25


def my_func():
    prefix = "value of 'a' is"
    print(f'{prefix} {a}')


my_func()
print(globals()['a'])
print(globals()['my_func'])
globals()['my_func']()  # you can pass argument to my_func as: globals()['my_func']("koko")
