# https://www.youtube.com/watch?v=C2QfkDcQ5MU
class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return True


class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)


class Poodle(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)


class GoldenRetriever(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)


sammy = Samoyed('Sammy', 2, 10)
print(sammy.name, sammy.age, sammy.friendliness)
print(sammy.likes_walks())