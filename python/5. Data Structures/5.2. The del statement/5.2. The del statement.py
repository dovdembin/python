def del_():
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]  # [1, 66.25, 333, 333, 1234.5]

    del a[2:4]  # [1, 66.25, 1234.5]

    del a[:]  # []

    del a  # delete the entire a list
