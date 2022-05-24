# https://www.youtube.com/watch?v=USkO5sRtnPE
"""
not good example because by adding more class we will have to add more if statements
"""
class Pacman:
    pass


class Ghost:
    pass


sprites = [
    Pacman(),
    Ghost()
]

for s in sprites:
    if isinstance(s, Pacman):
        print("Pacman")
    else:
        print("Ghost")
