class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()
print(x.f())  # hello world

print(MyClass.f(x))  # hello world

xf = x.f
print(xf())  # hello world
