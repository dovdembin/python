def in_():
    # in string
    my_string = "dov dembin"
    if "dov" in my_string:
        print("dov is in my_string")

    # empty string always true
    if "" in "abc":
        print("empty is in string")

    # in is like find
    if my_string.find("v") != -1:
        print("is in with find: " + str(my_string.find("v")))

    # in list
    fruits = ["apple", "banana", "cherry"]
    if "banana" in fruits:
        print("yes")

    # in dictionary
    dictionary = {"a": "my_a", "b": "my_b"}
    if "a" in dictionary:
        print("yes is in dictionary")

    # ======== in use with loop ===============
    fruits = ["apple", "banana", "cherry"]

    for x in fruits:
        print(x)


def not_in_():
    fruits = ["apple", "banana", "cherry"]

    if "koko" not in fruits:
        print("yes")


in_()
