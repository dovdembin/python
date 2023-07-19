programming_dictionary = {
    "key1": "value1",
    "key2": "value2"
}

#retrieve item
print(programming_dictionary["key1"])

#adding new items to dictionary
programming_dictionary["key3"] = "value3"
print(programming_dictionary)

#Create and empty dictionary
empty_dictionary = {}

#Edit and item in a dicrionary
programming_dictionary["key1"] = "value11"
print(programming_dictionary)


#Loop through a dictionary
for (key) in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

### Both dict() and {} will create an empty dictionary


x = dict(name = "John", age = 36, country = "Norway")
print(x)

x2 = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(x2)



