from abc import ABC, abstractmethod


class Absclass(ABC):
    def print(self, x):
        print("Passed value is ", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")


class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")


class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")


class error_example(Absclass):
    def simple_method(self):
        print("kaki")

    # this must be implemented
    # def task(self):
    #     print("this must be implemented")


test_obj = test_class()
test_obj.task()
test_obj.print(100)

example_obj = example_class()
example_obj.task()
example_obj.print(100)

print("is test_obj instance of Absclass?", isinstance(test_obj, Absclass))
print("is test_obj instance of Absclass?", isinstance(example_obj, Absclass))

error_instantiate = error_example()
error_instantiate.simple_method()
