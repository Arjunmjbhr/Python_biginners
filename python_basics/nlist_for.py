'''
- collection of list. Eacch list is an item 
- Each list is a row with columns within the collection
- list are zero indexed

'''


print("Nested List and For Loops...")

fruits = [
    ["Apples", "Berries", "Kiwi"],
    ["Oranges", "Berries", "Plum"],
    ["Mangos", "Bananas", "coconuts"],
    ["Pineapples"]
]

print(fruits)
print(" ")
print("Accessing Lists...")

# Elements can be accessed by their index.

print(" ")
print("0th row first column..")
print(fruits[0][1])
print(" ")
print("2nd row second column..")
print(fruits[2][2])

print(" ")
print("Print All Elements in the multidimention list")
for row in fruits:
    for col in row:
        print(col)
