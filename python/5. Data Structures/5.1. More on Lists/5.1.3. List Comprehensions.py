def list_comprehensions():
    """ These 2 are the same form of the list comprehensions
    def simple_loop():
        squares = []
        for x in range(10):
            squares.append(x ** 2)
        print(squares)

    def list_with_map():
        squares = list(map(lambda x: x ** 2, range(10)))
        print(squares)

    """

    def list_comprehensions_regular():
        squares = [x ** 2 for x in range(10)]
        print(squares)
        """ equivalent to:
            def simple_loop():
                squares = []
                for x in range(10):
                    squares.append(x ** 2)
                print(squares)

            def list_with_map():
                squares = list(map(lambda x: x ** 2, range(10)))
                print(squares)

        """

    def list_comprehensions_multiple_for():
        res = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
        """equivalent to:
        combs = []
        for x in [1,2,3]:
            for y in [3,1,4]:
                if x != y:
                    combs.append((x, y))
        """

    def some_example():
        vec = [-4, -2, 0, 2, 4]
        # create a new list with the values doubled
        res = [x * 2 for x in vec]  # [-8, -4, 0, 4, 8]

        # filter the list to exclude negative numbers
        res = [x for x in vec if x >= 0]  # [0, 2, 4]

        # apply a function to all the elements
        [abs(x) for x in vec]  # [4, 2, 0, 2, 4]

        # call a method on each element
        freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
        [weapon.strip() for weapon in freshfruit]  # ['banana', 'loganberry', 'passion fruit']

        # create a list of 2-tuples like (number, square)
        res = [(x, x ** 2) for x in range(6)]  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

        # the tuple must be parenthesized, otherwise an error is raised
        # [x, x ** 2 for x in range(6)]

        # flatten a list using a listcomp with two 'for'
        vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        res = [num for elem in vec for num in elem]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

        from math import pi
        [str(round(pi, i)) for i in range(1, 6)]  # ['3.1', '3.14', '3.142', '3.1416', '3.14159']

    some_example()