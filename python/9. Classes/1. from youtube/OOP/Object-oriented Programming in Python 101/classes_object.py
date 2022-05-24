"""
https://www.youtube.com/watch?v=wBhS8OXtM5Q
"""


class Pizza:
    """Models the idea of a Pizza."""
    # Attribute Definitions
    size: str
    toppings: int
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings
        # return self

    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza"""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0
        tax *= 8.0

        return total


a_pizza: Pizza = Pizza("large", 3)

print(Pizza)  # <class '__main__.Pizza'>
print(a_pizza)  # <__main__.Pizza object at 0x00000236EA17CDC0>
print(a_pizza.size)  # large
print(f"Price: ${a_pizza.price(1.05)}")
print(f"Price: ${Pizza.price(a_pizza, 1.05)}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")
