# ===========================================
def unpacked1():
    list_ = list(range(3, 6))  # normal call with separate arguments
    print(list_)

    args = [3, 6]
    list_ = list(range(*args))  # call with arguments unpacked from a list
    print(list_)


unpacked1()


def unpacked2(**kwargs):
    print(kwargs)  # {'key1': 'value1', 'key2': 'value2'}


unpacked2(**{"key1": "value1", "key2": "value2"})


def unpacked3(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
unpacked3(**d)


# =======================================================
# get will not raise error if not existing
def unpacked4(**kw):
    print(kw.get("koko"))

unpacked4(koko="kuku")

# [] will raise error if not existing
def unpacked5(**kw):
    print(kw["koko"])

unpacked5(koko="kuku")