def lambda_():
    """ This is how lambda is translated.

    "lambda" [parameter_list] ":" expression

    def <lambda>(parameters):
        return expression

    """
    def make_incrementor(n):
        return lambda x: x + n

    f = make_incrementor(42)
    print(f(0))

    print(f(1))

    # =================================
    def simple_example():
        x = lambda a: a + 10
        print(x(5))

    simple_example()

    def lambda_any_number_args():
        x = lambda a, b : a * b
        print(x(5, 6))

    lambda_any_number_args()

    # ============ this will sort according to the number or the word depend if pair[0] or pair[1]
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    pairs


print(lambda_.__doc__)