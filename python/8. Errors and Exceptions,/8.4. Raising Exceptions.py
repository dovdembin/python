def raise_():
    try:
        raise NameError('HiThere')
    except NameError:
        print("ok was raised")


def reraise_():
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by and will re raise another one to the air until!')
        raise


raise_()
reraise_()
