# functions returning other functions.


def greeting():
    def say_hello():
        return "Hello"
    return say_hello


hello = greeting()

print(hello())


# Assigning Functions to variables.

def mynum(x):
    return x+5


num = mynum

print(num(7))
print(mynum(10))


'''
 Global Vs Local Variable Scope

- Variables defined inside a function body have a local scope. 
- Variables defined outside a function have a global scope. 
- Global variables can be accessed anywhere in your python file. 
- Local variables can only be accessed inside the function it belogs to.

Using Global keyword

- This is to make the value of a local variable global. 

'''


x = 10


def my_numbers1():
    global x
    print("Global variable value", x)
    x = 7
    print("My Fav number is", x)


my_numbers1()
print(x)


# Nesting Functions


def mynum(a):
    def num(a):
        return a+1
    result = num(a)
    return result


print(mynum(5))
print(mynum(105))

# Nesting Function Accessing Variable Scope.


def display_message(message):
    "hello"
    def message_sender():
        "nested Function"
        print(message)
    message_sender()


display_message("Show me the Money!")
