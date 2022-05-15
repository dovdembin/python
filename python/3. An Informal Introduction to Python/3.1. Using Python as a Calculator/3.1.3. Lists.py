def examples():
    res = squares = [1, 4, 9, 16, 25]
    res = squares[0]  # indexing returns the item
    res = squares[-1]  # 25
    res = squares[-3:]  # [9, 16, 25]
    res = squares + [36, 49, 64, 81, 100]

    # ======== change content =================
    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 64

    # ======== append =================
    cubes.append(216)  # add the cube of 6
    cubes.append(7 ** 3)  # and the cube of 7

    # ======== Assignment to slices =================
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # replace some values
    letters[2:5] = ['C', 'D', 'E']
    # now remove them
    letters[2:5] = []
    # clear the list by replacing all the elements with an empty list
    letters[:] = []

    length = len(letters)  # built-in function len() also applies to lists:
    # print(length)

    # ======= nest lists ===========
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]  # [['a', 'b', 'c'], [1, 2, 3]]
    print(x[0])  # ['a', 'b', 'c']
    print(x[0][1])  # 'b'


def create_list():
    # an empty list
    empty = []
    # list of numbers
    nums = [10, 20, 30, 50]
    # list of strings
    words = ['cheerio', 'cheers', 'watcha', 'hiya']
    # list of mixed items
    anything = [10, 'hello', 'ahoy', 123.45]


def get_item_from_list():
    greetings = ['cheerio', 'cheers', 'watcha', 'hiya']
    res0 = greetings[0]
    res1 = greetings[3]
    res2 = greetings[1:3]
    print(f"{res0}, {res1}, {res2}")  # cheerio, hiya, ['cheers', 'watcha']


def append_to_list():
    # append to a list
    slang = ['cheerio', 'pip pip', 'smashing']
    slang.append('cheeky')
    slang.append('yonks')
    print(slang)  # ['cheerio', 'pip pip', 'smashing', 'cheeky', 'yonks']
    # same thing here
    slang = slang + ["koko"]
    print(slang)


def remove_from_list():
    # remove from a list
    slang = ['cheerio', 'pip pip', 'smashing', 'cheeky', 'yonks']
    # if we know the value
    slang.remove('cheeky')
    # if we know the index
    del slang[3]
    print(slang)  # ['cheerio', 'pip pip', 'smashing']
    # we can also delete a slice
    slang = ['cheerio', 'pip pip', 'smashing', 'yonks']
    del slang[:2]
    print(slang)  # ['smashing', 'yonks']


def adding_2_list():
    list1 = [4, 5, 2, 7]
    list2 = [2, 1, 3, 3]
    print(list1 + list2)


def list_filled_with_range():
    my_list_range = list(range(5, 10))
    print(my_list_range)
    my_list_range = list(range(0, 10, 3))
    print(my_list_range)
    my_list_range = list(range(-10, -100, -30))
    print(my_list_range)


if __name__ == "__main__":
    append_to_list()
