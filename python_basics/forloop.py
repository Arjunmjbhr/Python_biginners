'''
What is a for loop

> Used to iterate over a sequence. 
> Sequence is usually:(list,tuple,dictionary,set, string)
> Does not require an indexing variable to initiate loop. 
> They can use break and countinue statements. 

'''

fruits = ["grapes", "apples", "berries", "oranges"]

for x in fruits:
    print(x)

'''
Nested For Loop


- nested loop is a loop inside a loop
'''
print(" ")
colors = ["green", "yellow", "purple"]
fruits = ["apples", "banana", "berries"]

print("color list", colors)
print("fruits list", fruits)

print(" ")
print("nested loop results..")
print(" ")
for x in colors:
    for y in fruits:
        print(x, y)
