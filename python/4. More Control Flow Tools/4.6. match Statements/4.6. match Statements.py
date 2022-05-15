def match_():
    def match_1(status):
        match status:
            case 400:
                return "Bad request"
            case 404:
                return "Not found"
            case 418:
                return "I'm a teapot"
            case "dov":
                return "dembin"
            case _:  # this is a wildcard it will reach this if no match found
                return "Something's wrong with the internet"

    print(match_1("dov"))


def match_2(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


match_2((4, 5))


# ==================================================
class Point():
    __match_args__ = ("x", "y")

    def __init__(self, my_x, my_y):
        self.x = my_x
        self.y = my_y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


point = Point(0, 0)
where_is(point)


# ==================================================
def match_if(point):
    match point:
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print(f"Not on the diagonal")


match_if(point)


# ==================================================

def match_list(points):
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")


points = []
point1 = Point(0, 5)
points.append(point1)
point2 = Point(0, 4)
points.append(point2)
match_list(points)

# ==================================================
from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))


def name_constants(color):
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")


name_constants(color)
