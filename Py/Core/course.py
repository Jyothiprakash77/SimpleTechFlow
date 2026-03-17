# Q8. Create a class Course with:
# •	class variable total_students
# •	instance variable student_name
# •	instance method enroll() → increments total_students
# •	class method show_total(cls) → prints total students
# •	static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.
class course:
    total_students=0
    def __init__(self,name):
        self.Student_name=name
        self.enroll()
    def enroll(self):
        course.total_students+=1
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18
ram=course("ram")
sita=course("sita")
lakshman=course("lakshman")
course.show_total()