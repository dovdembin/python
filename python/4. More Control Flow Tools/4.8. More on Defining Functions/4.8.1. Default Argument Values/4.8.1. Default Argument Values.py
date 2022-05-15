def default_argument(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# This function can be called in several ways:
# default_argument('Do you really want to quit y/n?')
# default_argument('OK to overwrite the file y/n?', 2)
# default_argument('OK to overwrite the file y/n?', 2, 'Come on, only yes or no!')


# ========================================
def list_as_default_arguments(a, L=[]):
    L.append(a)
    return L


print(list_as_default_arguments(1))
print(list_as_default_arguments(2))
print(list_as_default_arguments(3))