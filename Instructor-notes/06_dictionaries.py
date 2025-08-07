# Dictionaries (Dict) - key-value pairs, unordered, mutable

adventurer = {
    "name": "Timothy", 
    "hitPoints": 10, 
    "belongings": ["sword", "shield", "potion", "tums", "water bottle"], 
    "companion": {
        "name": "Velma", 
        "type": "bat", 
        "companion": {
            "name": "Tim", 
            "type": "parasite", 
            "belongings": ["scuba tank", "ipod shuffle", "health insurance"]
        }
    }
}

# print(type(adventurer))
# print(adventurer["belongings"])  # Accessing a value by key

# for item in adventurer["companion"]["companion"]["belongings"]:
#     # print(f"item: {item} and it is a type {type(item)}")  # Iterating over a list in a dictionary
#     print(item.upper())

# # accessing keys and values in a dictionary
# print(adventurer.keys())
# # dict_keys(['name', 'hitPoints', 'belongings', 'companion'])

# print(adventurer.values())
# # dict_values(['Timothy', 10, ['sword', 'shield', 'p

# print(adventurer.items())
# dict_items([('name', 'Timothy'), ('hitPoints', 10), ('belongings', ['sword', 'shield', 'potion', 'tums', 'water bottle']), ('companion', {'name': 'Velma', 'type': 'bat', 'companion': {'name': 'Tim', 'type': 'parasite', 'belongings': ['scuba tank', 'ipod shuffle', 'health insurance']}})])


# ## loop over a dictionary
# for key, value in adventurer.items():
#     # print(f"{key}: {value}")  # Printing key-value pairs
#     print(key, value)


# .get()

# print(adventurer["loveLife"])
print(adventurer.get("loveLife" , "No love life found."))  # Using .get() to avoid KeyError

print(adventurer.update({"loveLife": "Complicated"}))  # Adding a new key-value pair
# print(adventurer)


# pop() - removes an item in dictionary by key

# print(adventurer.pop("name"))
# print(adventurer)


# if you want to remove the last added item from the dictionary
print(adventurer.popitem())  # Removes the last added key-value pair
print(adventurer)


# dict() - creates a dictionary from keyword arguments
new_dict = dict(name="John", age=30, city="New York")