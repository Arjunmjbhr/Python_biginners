'''
What is Abstraction

- Abstraction hides the internal details and shows only functionalities.

Abstract Classes

- They are classes that contain one or more abstract methods
- they cannot be instantiated. 
- They require subclasses to provide implimentation for the abstract methods.
- subclasses of an abstract class in Python are not required to impliment 
abstract methods of the parent class.

Abstract Methods

- They are methods that are declared but contains no implimentation. 
- Requires subclasses to provide implimentation for them.
'''

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


# myshape = Shape()
mysqure = Square(5)


# A B C => Abstract Base Classes
'''
A decorator allows you to add new functionality to an existing object
(classes,methods,functions) without modifying its structure.
'''
# Let us calculate the area and perimeter of the squre class instance(boject)
# called mysqure
print("Side value 5")
print("Area of Square = 5*5", mysqure.area())
print("Perimeter of Square 4 *5 = ", mysqure.perimeter())
