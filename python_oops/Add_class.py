'''
Creating a Class

- Created with the keyword class followed by a name. 
- Common Practice is to make the names Parcel Casing: Example MyFirstCar
- A class consists of variables(Attributes) and functions(Methods)
- Classes can be used to model a lot of things.

'''


class Instructors:
    CompanyName = "BlueLime"

    def __init__(self, course):
        self.course = course

    def printinfo(self):
        print("My company name is", Instructors.CompanyName)


'''
__init__() is a built-in function in python. Also known as the initilizer. 
used to initilize objects with initial values. All classes should have them.
It is called automatically when a new object is created from a class.



Self parameter is a reference to the current instance of the class. it is the 
first parameter of any method(function) in a class. it is used to access 
variables and methods belonging to the class. Also used to add attributes 
to a method.

'''

# Instantiating a Class

# The Process of creating an object from a class


elearning = Instructors("Python OOPs")

bls = Instructors("Django for Biginners")


# Accessing Methods
# ObjectName.Method


bls.printinfo()

# Accessing Attributes
# ObjectName.Attribute

print(bls.course)
print(elearning.course)
