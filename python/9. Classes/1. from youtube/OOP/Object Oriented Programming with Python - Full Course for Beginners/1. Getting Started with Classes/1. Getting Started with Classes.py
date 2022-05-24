#  https://www.youtube.com/watch?v=Ej_02ICOIgs


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  # Item.pay_rate (if we write this we will receive from class lever)


item1 = Item("Phone", 100, 1)

item1.apply_discount()
print(item1.price)


item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

# print(Item.__dict__)
# print(item1.__dict__)

# item1 = Item("Phone", 100, 1)  #  {'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x000002064C2DE8C0>, 'calculate_total_price': <function Item.calculate_total_price at 0x000002064C2DE950>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
# item2 = Item("Laptop", 1000, 3)  # {'name': 'Phone', 'price': 100, 'quantity': 1}

# print(type(item1))  # <class '__main__.Item'>
# print(type(item1.name))  # <class 'str'>
# print(type(item1.price))  # <class 'int'>
# print(type(item1.quantity))  # <class 'int'>
