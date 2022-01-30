'''
what is a tuple 

- a tuple is a list that can cannot changed.(immutable)
- Can be created using paranthesis. () and with a constructor. 
- Elements in a tuple can be accessed by their index. 

'''

# Normal List..
fruits = ("Grapes", "Apples", "Berries")

for x in fruits:
    print(x)

# Accessing the value of list
print(fruits[1])

# create a tuple with Construct

animals = tuple(("lion", "tiger", "bear"))
print(animals)

# Length of the Tuple
print(len(animals))

# Adding a new value to tuple gives you error.
# animals.add("Deer")

# print(animals)

# You can't change the value of tuple once it created..
animals[0] = "cheetah"
print(animals)

del animals
print(animals)
