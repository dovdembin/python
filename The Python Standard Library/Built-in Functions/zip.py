for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)
"""
(1, 'sugar')
(2, 'spice')
(3, 'everything nice')
"""
print(list(zip(range(3), ['fee', 'fi', 'fo', 'fum'])))  # [(0, 'fee'), (1, 'fi'), (2, 'fo')]

# list(zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True)) raise an error


print(list(zip(('a', 'b', 'c'), (1, 2, 3, 8))))


def tips_and_triks():
    x = [1, 2, 3]
    y = [4, 5, 6]
    list(zip(x, y))  # [(1, 4), (2, 5), (3, 6)]

    print(*zip(x, y))  # (1, 4) (2, 5) (3, 6)
    x2, y2 = zip(*zip(x, y))
    print(x2)  # (1, 2, 3)
    print(y2)  # (4, 5, 6)
    print(x == list(x2) and y == list(y2))  # True


tips_and_triks()