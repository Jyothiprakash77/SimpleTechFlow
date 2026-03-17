# Q10. Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.	Creates students
# 2.	Updates the passing criteria
# 3.	Displays grade category and result
class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.Name=name
        self.Marks=marks
    def result(self):
        if self.Marks>self.passing_marks:
            print(f"{self.Name} got passed")
        else:
            print(f"{self.Name} got failed")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>100 or marks<0:
            print("Invalid Input")
        elif marks>90:
            print("A")
        elif 90>marks>65:
            print("B")
        elif 65>marks>40:
            print("C")
Lankanna=Student("Lankanna",55)
Vaishnav=Student("Vaishnav",78)
Sai=Student("Sai",95)
Student.update_passing_marks(60)
Sai.result()
Vaishnav.result()
Lankanna.result()
Sai.grade_category(Sai.Marks)
Vaishnav.grade_category(Vaishnav.Marks)
Lankanna.grade_category(Lankanna.Marks)
