class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()

w2.region = 'east'
print(w2.purpose, w2.region)


# ========== method call method
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


b = Bag()
b.add(1)
b.addtwice(2)
print(b.data)
# ===============================
