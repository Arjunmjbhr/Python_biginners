'''
What is a python Dictionary?

A dictionary is a collection of key value pairs.

the values can be chaged (multiple).

the values have unique keys.

you can store mixed data types.

'''


mycar = {
    "brand": "Range Rover Sports",
    "model": "HSE",
    "year": 2017
}

print(mycar)

# Dictionary using constructor
mygreens = dict(fruit="Green Apples", vegitables="Kale")

print(mygreens)


# Bult in Dictionary Methods

'''

get() --> returns the value of specified key.
Update() --> Inserts a specified key:value pair in dictionary
clear() --> Removes all key:value pairs in dictionary
keys() --> returns a list of dictionary keys.
values() --> returns a list dictionary values. 
del() --> Deletes the dictionary

'''

print(len(mycar))  # No of key:value pairs
mycar["year"] = 2019  # change value of a key
print(mycar)
print(mycar.get("year"))  # get value of a key
mycar.update({"color": "Silver"})  # Adding a new value in the dictionary
print(mycar)

b = mycar.keys()  # accessing keys from the dictionary
print(b)

mycar.pop("color")  # removes an item pair
print(mycar)

mycar.clear()
print(mycar)

del mycar
print(mycar)
