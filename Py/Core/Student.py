class Student:
    def __init__(self,name,mark):
        self.Name=name
        self.Marks=mark
    def is_passed(self):
        if self.Marks>40:
            return True
        else:
            return False
Ashsravath=Student("Ashsravath",39)
print(Ashsravath.is_passed())
