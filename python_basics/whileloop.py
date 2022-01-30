'''
- Used to execute a set of statements(code)
countinuously as long as condition is True

while loop can have optional else clause. 

Syntax

    while text_expression:
        code to execute

'''

i = 1

while i <= 5:
    print(i)
    i += 1

# multiplecation table example for while


n = input("Enter an Integer Value: ")

i = 1
print("Multiplication table of ", n)
while i <= 10:
    print(n, " * ", i, " = ", int(n) * int(i))
    i += 1
