# https://www.youtube.com/watch?v=WYZrLtFNDVI
a = 35


def my_func(inp_param):
    local_var = "some string"
    print(inp_param, local_var)


print(globals())
print(globals()['a'])
print(globals()['my_func'])
globals()['my_func']("this is")

print(my_func.__code__.co_varnames)