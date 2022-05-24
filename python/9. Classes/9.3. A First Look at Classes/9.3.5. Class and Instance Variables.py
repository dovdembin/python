class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)  # canine
print(e.kind)  # canine
print(d.name)  # Fido
print(e.name)  # Buddy
print("=========================")
Dog.kind = "bulldog"
print(d.kind)  # bulldog
print(e.kind)  # bulldog
print(d.name)  # Fido
print(e.name)  # Buddy
print("=========================")
d.kind = "chihuahua"
print(d.kind)  # chihuahua
print(e.kind)  # bulldog
print(d.name)  # Fido
print(e.name)  # Buddy
print("=========================")
f = Dog('Snoopy')
print(f.kind)  # bulldog
print(f.name)  # Snoopy
