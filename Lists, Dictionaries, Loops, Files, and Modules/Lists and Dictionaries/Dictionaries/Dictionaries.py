def create_dictionaries():
    # create dictionaries
    slang = {'cheerio': 'goodbye', 'knackered': 'tired', 'yonks': 'ages'}
    # to look up a value
    print(slang['cheerio'])  # goodbye

    # Dictionary of strings to strings
    slang = {'cheerio': 'goodbye', 'knackered': 'tired'}
    # Dictionary of strings to numbers
    menu = {'spam meal': 15, 'spam with fries': 10}
    # Dictionary of anything
    anything = {10: 'hello', 2: 123.45}


def adding_items():
    # adding items
    slang = {}
    slang['cheerio'] = 'goodbye'
    slang['smashing'] = 'terrific'
    slang['knackered'] = 'tired'
    print(slang)
    # update item just look up item and assing
    slang['smashing'] = 'awesome'
    print(slang['smashing'])  # awesome


def delete_item():
    # delete item
    slang = {'cheerio': 'goodbye', 'knackered': 'tired', 'yonks': 'ages'}
    del slang['cheerio']  # del will delete the key-value pair
    print(slang)  # {'knackered': 'tired', 'yonks': 'ages'}


def access_key():
    slang = {'knackered': 'tired', 'yonks': 'ages'}
    # access key that does not exists will cause an error
    # insteed use get if exist key is return if not None is return
    result = slang.get('cheerio')
    if result:  # None
        print(result)
    else:
        print("Key doesn't exists")

    # this will raise an exception
    slang['cheerio']  # KeyError: 'cheerio'


access_key()
