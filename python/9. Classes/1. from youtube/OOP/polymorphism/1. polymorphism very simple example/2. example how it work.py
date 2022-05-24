# https://www.youtube.com/watch?v=USkO5sRtnPE

class Pacman:

    def draw(self):
        print("Pacman")


class Ghost:

    def draw(self):
        print("Ghost")


class Fruit:

    def draw(self):
        print("Fruit")


sprites = [
    Pacman(),
    Ghost(),
    Fruit()
]

for s in sprites:
    s.draw()

