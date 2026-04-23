class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>Student.passing_marks:
            return "Pass"
        return "Fail"
    @classmethod
    def Update_pass(cls,newpass):
        cls.passing_marks=newpass
    @staticmethod
    def grade_category(marks):
        if marks>85 and marks<=100:
            print("A")
        elif marks>65 and marks<=85:
            print("B")
        elif marks>40 and marks<=65:
            print("C")
        else:
            print("D")
S1=Student("Sai",90)
S1.Update_pass(95)
print(S1.result())
S1.grade_category(S1.marks)