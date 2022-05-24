class Complex:
    a = 101

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


print(Complex.a)
x = Complex(3.0, -4.5)
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
