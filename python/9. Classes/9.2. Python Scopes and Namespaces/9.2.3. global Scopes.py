# https://www.youtube.com/watch?v=WYZrLtFNDVI
a = 25


def my_func():
    global a  # if no global is set UnboundLocalError: local variable 'a' referenced before assignment
    prefix = "value of 'a' is"
    print(f'{prefix} {a}')
    a = 35


my_func()
print(a)
