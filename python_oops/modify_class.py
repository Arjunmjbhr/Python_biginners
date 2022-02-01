'''
Modifying a Class

- Add new Attributes
- Modify existing attribute valus
- Delete Attributes.

'''


class Instructors:
    CompanyName = "BlueLime"

    def __init__(self, course, duration):
        self.course = course
        self.duration = duration

    def printinfo(self):
        print("My company name is", Instructors.CompanyName)


elearning = Instructors("Python OOPs", 7)

bls = Instructors("Django for Biginners", 8)

bls.printinfo()


print("My Course Name is: ", bls.course)
print("My Course Duration is: ", bls.duration)

print("My Course Name is: ", elearning.course)
print("My Course Duration is: ", elearning.duration)

bls.course = "HTML"  # Modifying Couse Value

print("My Course Name is: ", bls.course)

del bls.duration
print(bls.duration)
