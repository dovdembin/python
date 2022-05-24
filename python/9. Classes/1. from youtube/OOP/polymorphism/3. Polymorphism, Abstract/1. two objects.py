# https://www.youtube.com/watch?v=8VAG5RfZVYc

class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def area(self):
        return self.l * self.w


class Square:
    def __init__(self, side):
        self.s = side

    def area(self):
        return self.s ** 2


rec = Rectangle(10, 20)
squ = Square(10)
print("Area of rectangle is:", rec.area())
print("Area of square is:", squ.area())
