def create_list():
    # an empty list
    empty = []
    # list of numbers
    nums = [10, 20, 30, 50]
    # list of strings
    words = ['cheerio', 'cheers', 'watcha', 'hiya']
    # list of mixed items
    anything = [10, 'hello', 'ahoy', 123.45]

def get_item_from_list():
    greetings = ['cheerio', 'cheers', 'watcha', 'hiya']
    res0 = greetings[0]
    res1 = greetings[3]
    res2 = greetings[1:3]
    print(f"{res0}, {res1}, {res2}")  # cheerio, hiya, ['cheers', 'watcha']

def append_to_list():
    # append to a list
    slang = ['cheerio', 'pip pip', 'smashing']
    slang.append('cheeky')
    slang.append('yonks')
    print(slang)  # ['cheerio', 'pip pip', 'smashing', 'cheeky', 'yonks']

def remove_from_list():
    # remove from a list
    slang = ['cheerio', 'pip pip', 'smashing', 'cheeky', 'yonks']
    # if we know the value
    slang.remove('cheeky')
    # if we know the index
    del slang[3]
    print(slang)  # ['cheerio', 'pip pip', 'smashing']
    # we can also delete a slice
    slang = ['cheerio', 'pip pip', 'smashing', 'yonks']
    del slang[:2]
    print(slang)  # ['smashing', 'yonks']
