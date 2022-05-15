tel = {'jack': 4098, 'sape': 4139}


def assign_and_print():
    tel['guido'] = 4127
    print(tel)  # {'jack': 4098, 'sape': 4139, 'guido': 4127}
    print(tel['jack'])  # 4098


def delete_item():
    del tel['sape']
    tel['irv'] = 4127
    print(tel)  # {'jack': 4098, 'guido': 4127, 'irv': 4127}


def return_keys():
    print(list(tel))  # ['jack', 'guido', 'irv']


def sort_keys():
    print(sorted(tel))  # ['guido', 'irv', 'jack']


def check_in():
    print('guido' in tel)  # True
    print('jack' not in tel)  # False


def dict_constructor():
    d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(d)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}
    # another way
    d2 = dict(sape=4139, guido=4127, jack=4098)
    print(d2)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}


def dict_comprehensions():
    dict_ = {x: x ** 2 for x in (2, 4, 6)}  # {2: 4, 4: 16, 6: 36}
    print(dict_)


assign_and_print()
delete_item()
return_keys()
sort_keys()
dict_constructor()
dict_comprehensions()
