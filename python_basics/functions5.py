# function pass keyword

def dream_home():
    pass

# Passing Functions as Arguments to other Functions.


def mynum(b):
    return b + 25


def addnum(c):
    newnum = 9
    return c(newnum)


print(addnum(mynum))


'''
varArgs Parameters

- Lets you define variable number of arguments for a function
- this is done using *

single * is a tuple
double * is a dictionary
'''


def total_num(a=7, *numbers, **phonebook):
    print("My Fav number is", a)

    for num in numbers:
        print("num", num)

    for name, phone_number in phonebook.items():
        print(name, phone_number)


total_num(7, 1, 2, 3, Jane=2222, John=4444, Angela=5555)


# Python built-in Functions and Methods..

'''

What is a Python Function .. 


- A function is a block of code that does something specific

- It is called or invoked by their name. Example print()

- It can be passed data or parameter to use inside paranthesis()


What is a Python Method

- A method is like a function.
- it is avaliable for a given object data type.
- example "hello" (string)
- Methods are invoked or called by object name. method name
- Example "hello".upper()

'''
print(" ")
print("Python Functions and Methods..")
b = "hello"

print(len(b))
print(b.upper())
