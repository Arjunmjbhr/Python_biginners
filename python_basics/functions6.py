# Anonymous Functions (Lambda)

'''
They are defined using the lambda keyword.

they can take several arguments but can only have one expression.

a = lambda b: b+4
print(a(4))


c = lambda d,e : d +e
print(c(7,8))

Note: this file will show nothing to see the proper output open your python shell
and run the above code on their...

'''


def ghost_number(n):
    return lambda f: f * n


double_num = ghost_number(2)

print(double_num(20))


'''
DocStrings(Document String)

- Allows you to display code documentation when code executes. 
- They are accessed by using doub;e underscore with attribute name.
- They are defined using three single quotes and some text.

'''


def add_numbers(d, e):
    '''Adding two numbers. 

    the values must be integers
    '''
    print(d + e)


print(add_numbers.__doc__)
add_numbers(8, 4)
