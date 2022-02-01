'''
What is Inheritance 

- The process of creating new classes and reusing methods and attributes
from the parent class.

- The Parent Class (Superclass or base class) is the class been inherited from

- the Child class (subclass or derived) is the class that inherits from another 
class.


'''


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


print("Output From Parent Class")
print(" ")
florist = Person("Jane", "Flowes")
florist.printname()

'''
Please Note that if you create a child class without an __init__() method it 
inherits all methods and attributes of the parent class.
'''


class Lawyers(Person):
    pass


print(" ")
print("Output from the Child Class")
print(" ")
happy_layers = Lawyers("Jack", "Smiley")
happy_layers.printname()


class myinfo(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printinfo(self):
        print(self.firstname, self.lastname)


print(" ")
print("Output From the 3rd class")

myinfo1 = myinfo("Smith", "Johns")
myinfo1.printinfo()

# Please Note there is only one init in: __init__() even though i have mentioned
# two here.


class myInformation(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        # self.firstname = fname
        # self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


print(" ")
print("Output From the 4th class")

myinfo2 = myInformation("Smith", "Smily")
myinfo2.printname()

# Adding Attributes and methods to Child Class.


class myInformation2(Person):
    def __init__(self, fname, lname, casetype):
        Person.__init__(self, fname, lname)
        self.firstname = fname
        self.lastname = lname
        self.casetype = casetype

    def printinformation(self):
        print("Hello my name is ", self.firstname, self.lastname)


print(" ")
print("Output From the 5th class")

myinfo3 = myInformation2("Smith", "Smily", "criminal")
myinfo3.printinformation()
print(myinfo3.casetype)
