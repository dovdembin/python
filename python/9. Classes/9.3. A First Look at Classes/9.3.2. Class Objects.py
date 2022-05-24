class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


print(MyClass.i)
MyClass.i = 100
print(MyClass.i)
print(MyClass.__doc__)

x = MyClass()
print(x.f())
print(f"this is i: {MyClass.i}")
# ===========================================


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)
# ===========================================
