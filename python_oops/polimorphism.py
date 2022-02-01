'''
What is Polimorphism ? 

Polymorphism means the ability to take or have various forms. 

Lets have an example 

you have a phone and the phone has Camera,Mp3 Player, Radio etc.

Polimorphism allows us to define methods in child class with same name as methods
in the parent class but doing different things.


print(len("Hello"))
print(len([20, 40, 30]))

'''


def addNumbers(a, b, c=30):
    return a + b + c


print(addNumbers(10, 20))  # passing arguments for the function parameters.

print(addNumbers(8, 9, 4))


# polimorphic class with parameters

print(" ")

print("Polimorphic Classes")


class UK():
    def capital_city(self):
        print("London is the capital of UK")

    def language(self):
        print("English is the primary Language ")


class Spain():
    def capital_city(self):
        print("Madrid is the capital of Spain")

    def language(self):
        print("Spanish is the primary Language ")


print(" ")
print("Output From UK Class")
queen = UK()
queen.capital_city()

print(" ")
print("Output From the Spain Class")
zara = Spain()
zara.capital_city()


print(" ")
print("Output from forloop")
for country in (queen, zara):
    country.capital_city()
    country.language()
# Create polymorphism by using existing method on a new function.


def europe(eu):
    eu.capital_city()


print(" ")
print("Polymorphic Function take output from other classes")
europe(queen)
europe(zara)
