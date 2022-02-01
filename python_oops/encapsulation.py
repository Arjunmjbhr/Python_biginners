'''
What is Encapsulation ? 

- Process of restructing access to methods and variables to prevent 
direct data modification. 


- Public methods and variables are accessable from anywhere in the program. 

- Private methods and variables are accessable from their own class. 

- Double underscore prefix before object name makes it private. 

'''


class Cars:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

# please be careful with your intendation.
    def get_speed(self):
        return self.__speed


ford = Cars(250, "Green")
nissan = Cars(300, "Red")
toyota = Cars(200, "Blue")

ford.set_speed(750)
ford.__speed = 500
print(ford.get_speed())

# print(ford.__color)


# Double underscore prefix before variable or method names make them private.
# Set Method is used to set value for variable while get method is used to
# retrive the value of the variable.
