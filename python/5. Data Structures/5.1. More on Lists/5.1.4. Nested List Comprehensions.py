def nested_list_comprehensions():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    res = [[row[i] for row in matrix] for i in range(4)]
    """Transpose rows and columns.
    [[1, 5, 9], 
    [2, 6, 10], 
    [3, 7, 11], 
    [4, 8, 12]]

    same as:

    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    which, in turn, is the same as:

    transposed = []
    for i in range(4):
        # the following 3 lines implement the nested listcomp
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    print(transposed)
    """