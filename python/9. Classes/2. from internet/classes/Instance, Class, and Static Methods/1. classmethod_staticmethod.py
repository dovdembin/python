# =============after creating object=================
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
print(obj.method())  # ('instance method called', <__main__.MyClass object at 0x000001EF8AF82B60>)
print(obj.classmethod())  # ('class method called', <class '__main__.MyClass'>)
print(obj.staticmethod())  # static method called


# =================before creating object=================


class MyClass2:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


print(MyClass2.classmethod())  # ('class method called', <class '__main__.MyClass2'>)

print(MyClass2.staticmethod())  # static method called

# print(MyClass2.method())  # TypeError: MyClass2.method() missing 1 required positional argument: 'self'


