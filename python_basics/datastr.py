'''
Data Structure 

- They structures which can hold some data together. 
- they are used to store a collection of related data. 
- Python has the following built-in data structures. 

* List
* Tuple
* Set 
* Dictionary
'''


print("Data structures of python...")
print("python List")
'''
What is a List..

A list is a collection if data which can be mixed type.

items in a list are ordered by their index and changable. 

Lists are created with square brackets. []

items in a list can assessed by their index.


'''
animals = ["Bear", "Lion", "Tiger", "Panda", "Elephant"]
for x in animals:
    print(x)

print(animals)

print(" ")

print("Accessing Elements of Lists..")

'''
A can be accessed using their index or position in the list

the index is zero based. First element has a position of zero

'''

animals = ["Bear", "Lion", "Tiger", "Panda", "Elephant"]

print("animals[0]", animals[0])
print("animals[2]", animals[2])
print("animals[4]", animals[4])

print(animals[1:])
print(animals[1:3])

print("Changing List Values.")

animals[0] = "cheeta"

print("animals[0] value changed", animals[0])

print(" ")
print("Python List Methods...")

fruits = ["Berries", "Apples", "Grapes", "Oranges"]
vegitables = ["Kale", "Broccoli", "Lettuce"]
print(" ")
print("List 1: ", fruits)
print("List 2: ", vegitables)
print(" ")
print("exted() result")
fruits.extend(vegitables)

print(fruits)

print(" ")

print("Append Result")

vegitables.append("bean")

print("appended beans on vegitables: ", vegitables)


print(" ")

print("Sort list..")

vegitables.sort()
fruits.sort()

print(" ")
print("Vegitables sorted", vegitables)
print("fruits sorted", fruits)


vegitables.sort(reverse=True)
fruits.sort(reverse=True)

print(" ")
print("Vegitables reverse sorted..: ", vegitables)
print("Fruits reverse sorted: ", fruits)


print("Count method in lists")

print("there are ", fruits.count("Apples"), "Apples in the list")

print(" ")
print(" index() method")

print("index value of Grapes is: ", fruits.index("Grapes"))

print(" ")

print("Insert methods..")

fruits.insert(0, "Banana")

print("Banana is added on index 0: ", fruits)

print(" ")
print("POP method")
print(fruits)
fruits.pop()
print("Last index value is popped from the list..", fruits)


print(" ")
print("Remove Method..")
print(" ")
print(vegitables)
vegitables.remove("Lettuce")

print("Lettuce is removed from the vegitables list..", vegitables)

print(" ")
print("del method..")

del vegitables
print(vegitables)
