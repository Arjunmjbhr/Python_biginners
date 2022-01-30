'''
What are functions ? 

- Functions are pieces(block) of code that does something. 
- They are reusable
- They execute or run when called by their name. 
- They can have parameters(variables) and arguments(values)
- they can return data as a result. 
- there are built-in functions. Example print()
- You can also create your own custom functions.

Creating a function

- Descriptive names.
- Same naming rules as variables. 

def function_name():
    print("Hello world!")
'''


def sum(x, y):
    print(x + y)


'''
Calling a Function

- Also known as: running, executing, invoking
- You can call a function by it's name and add paranthesis. 
- Any parameters or arguments are placed inside the paranthesis.
'''

sum(3, 5)

'''
Parameter Vs Argument

A parameter is a variable defined inside a function's paranthesis. 

An argument is the actual value you pass(give) the function when it is called. 


'''

# Return Value
# this is used inside a function to return a value.


def sum1(x, y):
    return x+y


print(sum1(4, 5))
print(sum1(10, 30))

'''
Default Parameter Value

- this is the value a function uses when called without passing it a value.
- Only parameters at the end of a parameter list can have a default value as 
Values are assigned by position.

def greeting(a,b=7) 
def greeting(a=6,b) 
'''


def student_names(names="Bluelime"):
    print("Hello " + names)


student_names()
student_names("John")
student_names("Jane")

'''
Keyword Arguments

- allows you to specify what parameters to use from a list of parameters.
- You do not need to worry about the order of the arguments.
- Allows you to give values only to parameters you want provided the other 
parameters have default argument values. 
'''


def more_num(a, b=7, c=10):
    print("a is ", a, "and b is ", b, "while c is", c)


more_num(7, 10, 4)
more_num(23, c=25)
more_num(c=40, a=80)
