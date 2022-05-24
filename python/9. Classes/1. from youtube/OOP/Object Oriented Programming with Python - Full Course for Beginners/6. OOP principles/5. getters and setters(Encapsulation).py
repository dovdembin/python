#  https://www.youtube.com/watch?v=Ej_02ICOIgs

from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3)
item2 = Phone("jscPhone", 500, 3)
# item1.apply_increment(0.2)
item1.apply_discount()
item2.apply_discount()
# print(item1.price)

print(item2.price)
print(item1.price)
