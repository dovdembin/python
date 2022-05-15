fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')  # 2
fruits.index('banana')  # 3
fruits.index('banana', 4)  # Find next banana starting a position 4 return 6
fruits.index("kiwi", 0, 7)  # Raises a ValueError if there is no such item
fruits.reverse()  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')  # Equivalent to a[len(a):] = [x]
fruits.sort()  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()  # return pear, remove pear from the list
fruits.insert(0, 'peach')  # ['peach', 'apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
fruits.pop(0)  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
copy_fruits = fruits.copy()  # Equivalent to a[:]
fruit_yami = ["blueberry", "strawberry"]
fruits.extend(fruit_yami)  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'blueberry', 'strawberry']
print(fruits)
fruits.clear()
print(copy_fruits)