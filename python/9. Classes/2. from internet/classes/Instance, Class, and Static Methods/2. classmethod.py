# https://realpython.com/instance-class-and-static-methods-demystified/
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


print(Pizza(['cheese', 'tomatoes']))  # Pizza(['cheese', 'tomatoes']) # it goes to __init__
print(Pizza.margherita())  # Pizza(['mozzarella', 'tomatoes'])
print(Pizza.prosciutto())  # Pizza(['mozzarella', 'tomatoes', 'ham'])