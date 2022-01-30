
# Arithamatic Operations

'''
used to perform mathematical Operations..

Operator       Name                     Example
+              Addition                 a+b
-              Subtraction              a-b
*              Multiplication           a*b
/              Division                 a/b
%              Modulus                  a%b
**             Power(Pow)               a**b
//             Floor Division           a//b

'''
print("Arithamatic Operations")
x = 7
y = 5

print("x=7 and y =5")
print("x+y =", int(x) + int(y))
print("x-y =", int(x) - int(y))
print("x*y =", int(x) * int(y))
print("x/y = ", int(x) / int(y))
print("x%y =", int(x) % int(y))
print("x power y =", int(x) ** int(y))
print("x //y =", int(x) // int(y), "floor divistion")
print("Hello " * 3, "(hello*3)")

print(" ")


# Assignment operators

'''
Used to assign values

Operator            Example             Equivalent 
=                   a=4                 a=4
+=                  a+=4                a=a+4
-=                  a-=4                a=a-4
*=                  a*=4                a=a*4
/=                  a/=4                a=a/4


'''
print("Assignment Operators")
a = 4
print("a =", a)
a += 5
print("a+=5", a)
a -= 3
print("a-=3", a)
a *= 4
print("a*=4", a)
a /= 2
print("a/=2", a)
a %= 5
print("a%=5", a)
a **= 3
print("a**=", a)
a //= 2
print("a//=2", a)


print(" ")
print("Comparison Operators")

'''

They are used to Compire Values..

Operator            Value
==                  Equal.
!=                  Not Equal.
>                   Greater than
<                   Less than
>=                  Greater than or equal to
<=                  Less than or equal to 
'''


print(" ")
a = 5
b = 6
print("a==b is", a == b)

print("a!=b is", a != b)

print("a>b is", a > b)

print("a<b is", a < b)

print("a>= is", a >= b)

print("a<= b is", a <= b)

print(" ")

print("Logical Operators..")

'''
They are used to combine conditional Statements. 

Operator                Description
and                     Returns true if all conditions true. 
or                      Returns true eaither condition is true.
not                     Returns false if result is true

'''


print(" ")

# input from users...

print("a>6 and a<9 is", a > 6 and a < 9)
print("a>6 or a<5 is", a > 6 or a < 5)
print("not(a>6 and a<9) is", not(a > 6 and a < 9))
