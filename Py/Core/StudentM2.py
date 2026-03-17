#M2
# Q1. Create a class Student that:
# •	Keeps track of the total number of students created.
# •	Determines whether a student passed or failed based on a shared passing mark.
# •	Provides a method to curve marks by increasing everyone’s marks by a percentage.
# •	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
# Demonstrate:
# 1.	Creating multiple students.
# 2.	Applying a grading curve.
# 3.	Displaying updated results with letter grades.
class Student:
    Total_students=0
    Student_Details=[]
    # @staticmethod
    # def add_student(fun):
    #     def wrapper(*args,**kwargs):
    #         obj=fun(*args,**kwargs)
    #         Student.Student_Details.append(obj)
    #         return obj
    #     return wrapper
    # @add_student
    def __init__(self,id,marks):
        Student.Student_Details.append(self)
        self.id = id
        self.mark=marks
        Student.Total_students+=1
    def passcretiria(self,pass_mark):
        if self.mark>pass_mark:
            print("Student got passed")
        else:
            print("Student got failed")
    @classmethod
    def increase_curve(cls,percentage):
        for i in Student.Student_Details:
            inc=i.mark*(percentage/100)
            i.mark=i.mark+inc
    @staticmethod
    def Grade_curve(marks):
        if marks>100 or marks<0:
            return 0
        elif marks>=85:
            return "A"
        elif marks>=65:
            return "B"
        elif marks>=45:
            return "C"
        elif marks>=36:
            return "D"
        else:
            return "F"
s1=Student(1,78)
s2=Student(2,36)
s3=Student(5,54)
print(s1.mark)
s1.increase_curve(10)
for i in Student.Student_Details:
    print(f"{i.mark}->{i.Grade_curve(i.mark)}")
    i.passcretiria(36)
# the system i designed was able to store the marks keep the total students track ,increase the marks for everybody,i can retrive the marks
# , can show pass or failed and generate grades