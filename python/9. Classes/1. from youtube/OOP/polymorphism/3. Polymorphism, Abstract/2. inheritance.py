# https://www.youtube.com/watch?v=8VAG5RfZVYc

class Human:
    def who_am_i(self):
        print("I am a Human")


class Teacher(Human):
    def who_am_i(self):
        print("I am a Teacher")


t = Teacher()
t.who_am_i()
