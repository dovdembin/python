from enum import Enum

# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# functional syntax
Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])

some_var = Color.RED
print(some_var in Color)