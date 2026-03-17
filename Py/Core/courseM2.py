#M2
# Q5. Create a class Course that:
# •	Tracks total courses created.
# •	Each course has a title, duration, and enrolled_students.
# •	Provides a method to enroll a new student.
# •	Allows updating the minimum duration for a valid course across all instances.
# •	Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# 1.	Creating multiple courses.
# 2.	Enrolling students.
# 3.	Updating minimum duration and checking durations.
class Course:
    Total_course=[]
    min_Duration=0
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
        self.enrolled_student={}
        Course.Total_course.append(self)
    def Enroll_student(self,name,age):
        self.enrolled_student[name]=age
    @classmethod
    def change_minDuration(cls,newMD):
        cls.min_Duration=newMD
    @staticmethod
    def check_duration(Drt,min_Drt):
        if Drt<=min_Drt:
            return "Invalid Duration"
        else:
            if Drt>6:
                return "Invalid Duration"
            else:
                return "Valid Time"
Digital_Marketing=Course("Digital Marketing",4)
Java=Course("JAVA",6)
Medical_coding=Course("Medical coding",4)
Java.Enroll_student("Gowramudi narendra",22)
Java.Enroll_student("Parvathaneni Pavan Kumar",22)
Medical_coding.Enroll_student("Althi Dilip",23)
print(Java.enrolled_student)
Course.min_Duration=4
print(Java.duration)
print(Medical_coding.check_duration(Medical_coding.duration,Medical_coding.min_Duration))
