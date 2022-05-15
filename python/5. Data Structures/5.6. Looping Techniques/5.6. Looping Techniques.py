knights = {'gallahad': 'the pure', 'robin': 'the brave'}


def key_value():
    for k, v in knights.items():
        print(k, v)
    """
        gallahad the pure
        robin the brave
    """


def index_position_loop_over_sequence():
    # When looping through a sequence, the position index and corresponding
    # value can be retrieved at the same time using the enumerate() function.
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
    """
        0 tic
        1 tac
        2 toe
    """


def zip_two_or_more_sequences_at_the_same_time():
    # see zip() function.
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))
    """
        What is your name?  It is lancelot.
        What is your quest?  It is the holy grail.
        What is your favorite color?  It is blue.
    """


def reverse_over_sequence():
    for i in reversed(range(1, 10, 2)):
        print(i)
    """
        9
        7
        5
        3
        1
    """


def sorted_source_does_not_change():
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for i in sorted(basket):
        print(i)
    """
        apple
        apple
        banana
        orange
        orange
        pear
    """


def set_loop():
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)
    """
        apple
        banana
        orange
        pear
    """


def best_to_create_new_list():
    import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)

    print(filtered_data)  # [56.2, 51.7, 55.3, 52.5, 47.8]


key_value()
index_position_loop_over_sequence()
zip_two_or_more_sequences_at_the_same_time()
reverse_over_sequence()
sorted_source_does_not_change()
set_loop()
best_to_create_new_list()