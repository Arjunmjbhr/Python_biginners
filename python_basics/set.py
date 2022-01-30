# What is a set.

# 1) A set us a collection of values.
# 2) Values in a set are not ordered.
# 3) Values in a set are not indexed.
# 4) you can add values to a set but not change values.

# How to create a Set.


fruits = {"grapes", "apples", "berries"}

for x in fruits:
    print(x)

'''
how to create a set with a constructor

animals = set(("lion","tiger","bear"))
'''

animals = set(("lion", "tiger", "bear"))
animals = (("lion", "tiger", "bear"))

'''
 Note: if you do not add the keyword set to the constructor. it will create a
 tuple datatype.
'''
print(len(animals))

'''

built in set methods

add()  --> adds an element to a set.
Update() --> adds multiple elements to a set. 
clear() --> removes all elements in a set
discard() --> removes a specified element or item
remove() --> Removes a specified item from the set
del() --> Deletes the set
'''

fruits.add("oranges")

print(fruits)

fruits.update(["mango", "banana", "kiwi"])
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.clear()
print(fruits)

del animals
print(animals)
