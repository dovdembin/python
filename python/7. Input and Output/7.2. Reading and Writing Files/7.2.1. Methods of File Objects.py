"""Mode can be.
'r' when the file will only be read,
'w' for only writing (an existing file with the same name will be erased),
'a' opens the file for appending,
'r+' opens the file for both reading and writing
"""


def open_():
    f = open('workfile', 'r', encoding="utf-8")
    print(f.read())
    f.close()


def open_with():
    with open('workfile', encoding="utf-8") as f:
        print(f.read())


def override_():
    with open('workfile', 'w', encoding="utf-8") as f:
        f.write("Agadol")
    open_with()


def appending_():
    with open('workfile', 'a', encoding="utf-8") as f:
        f.write(" mikulam\ntoda it is nice\nakol tov")
    open_with()


def read_example():
    with open('workfile', encoding="utf-8") as f:
        print(f.read(2))  # at most size characters (in text mode) or size bytes (in binary mode) are read and returned

    with open('workfile', encoding="utf-8") as f:
        print(f.readline())

    with open('workfile', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
            print()

    with open('workfile', encoding="utf-8") as f:
        print(f.readlines())  # read all the lines of a file in a list you can also use list(f)

    with open('workfile', 'w', encoding="utf-8") as f:
        value = ('the answer', 42)
        s = str(value)  # convert the tuple to string
        f.write(s)

    with open('workfile', encoding="utf-8") as f:
        print(f.tell())


def byte_():
    f = open('workfile', 'rb+')
    f.write(b'0123456789abcdef')
    f.seek(5)  # Go to the 6th byte in the file
    print(f"this is seek(5) {f.read(1)}")
    f.seek(-3, 2)  # Go to the 3rd byte before the end
    print(f.tell())
    print(f.read(1))
    f.close()


open_()
open_with()
override_()
appending_()
read_example()
byte_()