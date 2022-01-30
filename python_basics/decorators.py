'''
- Decorators are used to add new functionality to existing objects like functions,
methods and classes without modifying it's structure.

- Decorators are usually called before the definision of the object 
(Function,Method,Class) we want to decorate.

- They can be represented by @ followed by name of the decorated object.


Creating a Decorator

Convert sentence to uppercase
'''


def my_decorator(function):
    def wrapper():
        myfunc = function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wrapper


@my_decorator
def say_hello():
    return "Hello python"


decorator = my_decorator(say_hello)
print(decorator())

# To learn more about decorator
# https://www.python.org/dev/peps/pep-0318/
