# What makes generators so compact is that the __iter__() and __next__() methods are created automatically.

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)
