### class attributes or instance attributes
```python 
class Banana:
    """A tasty tropical fruit"""
    food_group = 'fruit'
    colors = ['green', 'green-yellow', 'yellow','brown spotted', 'black']
```
### instance method
 ```python
class Banana:
    def peel(self):
    self.peeled = True
```
self it's passed implicitly
```python
my_banana = Banana()
my_banana.set_color('green')
my_banana.peel()
```
### class methods 
#### do not have access to the instance of the class and cannot read or write instance attributes  
***cls*** is implicitly passed a reference to the class as the first argument
```python
@classmethod
 def check_color(cls, color):
 """Test a color string to see if it is valid."""
 return color in cls.colors
@classmethod
 def make_greenie(cls):
 """Create a green banana object"""
 banana = cls()
 banana.set_color('green')
 return banana
```
### static methods
```python
@staticmethod
 def estimate_calories(num_bananas):
 """Given `num_bananas`, estimate the number of calories"""
 return num_bananas * 105
```
### magic attributes and magic methods (***or dunder methods***)
```python
def __init__(self, color='green'):
 if not self.check_color(color):
 raise ValueError(
 f'A {self.__class__.__name__} cannot be {color}'
 )
 self.color = color
```
### Public members,  Protected members, Private members
#### these are merely conventions
__var Private members
_var Protected members
var Public members

### Inheritance
```python
class RedBanana(Banana):
 """Bananas of the red variety"""
 pass
```
