'''
Control Flow

What is Control Flow

- this is the order in which the program's code executes.
- they help your program make dicisions. 
- The control flow of a python program is regulated by
    
    > conditional statements
    > loops
    > function calls.      

What can be used with control flow.

* Conditional Statements(if,elif,else) are statements that only run based on 
certain conditions.

* Loops are used to repeat a specific block of code.(for and while)

* a function is a piece of code that does something specific. 

* A function call is when you a functions is called by it's name to 
execute a code. Example print().
'''

# if statements?
'''

What are if statements ? 

- used to check condition before executes certain code. 
- they help your program make dicitions. 
- they only run code in if-block when condition is True. 
- They use comparison and logical operators to check conditions.

Syntax for if statements

if(condition): 
    indented statement Block

'''

a = 7
b = 8

print("a =", a, "and b =", b)
if a < b:
    print(a, "is less than", b)

'''
What are else statements?

- Code that executs if condition checked evaluates to False.


syntax for else statements

if(condition1):
    Intended statement block for condition 1
elif(condition2):
    indended statement block for condition 2
else:
    Alternate statement block if all condition above fails
'''

x = 7
y = 8
z = 9

print("x =", x, "y =", y, "and z =", z)
if x > y:
    print(x, "is smaller than", y)
elif y >= z:
    print(b, "is smaller than", z)
else:
    print(z, "is larger than", x, "and", y)

'''
elif statements

What are elif statements ? 

- used to check multipl expression for true conditions.

- only executes a block of code as soon as one of the 
conditions evaluates to True

Syntax elif statements

if(condition1):
    Indented statement block for condition 1
elif(condition2):
    Indented statement block for condition 2

'''

a = 30
b = 40

if a > b:
    print(a, " is smaller than", b)
elif b > a:
    print(b, "is bigger than", a)
