class Dog:
    # this static thing effects only mutable objects such as lists and dictionaries
    tricks = []  # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)  # unexpectedly shared by all dogs ['roll over', 'play dead']
print(e.tricks)  # unexpectedly shared by all dogs ['roll over', 'play dead']


class Dogy:  # correct way

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dogy('Fido')
e = Dogy('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)  # ['roll over']
print(e.tricks)  # ['play dead']
