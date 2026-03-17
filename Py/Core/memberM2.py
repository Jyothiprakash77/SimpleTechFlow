#M2
# Q10. Create a class Member that:
# •	Has a shared BMI limit for “fit” status.
# •	Each member stores name, height, weight.
# •	Has a method to calculate BMI and check fit status.
# •	Provides a function to update BMI limit for all members.
# •	Offers a tool to check if height and weight entered are valid numbers.
# Demonstrate:
# 1.	Creating multiple members.
# 2.	Updating BMI standard.
# 3.	Displaying fit status and input validity.
class Member:
    BMI_MIN=18.5
    BMI_MAX=25
    def __init__(self,name,height,weight):
        if Member.valid(height,weight):
            self.name=name
            self.height=height
            self.weight=weight
        else:
            print("Invalid inputs")
    def fit_status(self):
        bmi=(self.weight//self.height**2)*703
        if self.BMI_MIN<=bmi and bmi<=self.BMI_MAX:
            print(f"{self.name} is fit")
            return True
        else:
            print(f"{self.name} is not fit")
            return False
    @classmethod
    def change_BMI(cls,new_BMIMIN=0,new_BMIMAX=0):
        if new_BMIMIN!=0:
            cls.BMI_MIN=new_BMIMIN
        if new_BMIMAX!=0:
            cls.BMI_MAX=new_BMIMAX
    @staticmethod
    def valid(height,weight):
        if height<=0 or weight<=0:
            return False
        return True
Hemanth=Member("Hemanth",5.5,67)
Krishna=Member("Krishna",5.3,-1)
Kuldeep_singh=Member("Kuldeep singh",5.9,75)
Member.change_BMI(20)
print(Member.BMI_MIN,Member.BMI_MAX)
Krishna.fit_status()



