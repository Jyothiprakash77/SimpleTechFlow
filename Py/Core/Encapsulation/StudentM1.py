# 2. Design a Student class where marks:
# • should always be between 0 and 100
# • should never be set directly
# Enable updating marks only through a controlled method that performs range
# checks.
# Demonstrate:
# • trying to assign marks manually
# • why encapsulation protects invalid states
class Student:
    def __init__(self):
        self.__marks=0
    def getMarks(self):
        return self.__marks
    def setMarks(self,marks):
        if marks>0 and marks<=100:
            self.__marks=marks
        else:
            print("Invalid Marks")

Ramesh=Student()
print(Ramesh.__marks)
# Ramesh.setMarks(89)
# print(Ramesh.getMarks())