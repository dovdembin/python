def tuples_and_sequences():  # Tuples are immutable
    t = 12345, 54321, 'hello!'
    print(t[0])  # 12345
    print(t)  # (12345, 54321, 'hello!')
    # Tuples may be nested:
    u = t, (1, 2, 3, 4, 5)  # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
    v = ([1, 2, 3], [3, 2, 1])  # ([1, 2, 3], [3, 2, 1])

    empty = ()
    singleton = 'hello',  # <-- note trailing comma ,tuple with 1 item is constructed by following a value with a comma
    len(empty)

    len(singleton)

    x, y, z = t = t
    print(x)  # 12345
    print(y)  # 54321
    print(z)  # hello!


tuples_and_sequences()