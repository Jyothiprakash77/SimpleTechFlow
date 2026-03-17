#M2
# Q3. Create an Employee class that:
# •	Keeps a minimum experience required for promotion (shared across all employees).
# •	Stores employee name, experience, and department.
# •	Has a method to check eligibility for promotion.
# •	Provides a function to update promotion criteria globally.
# •	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.	Creating employees from different departments.
# 2.	Changing promotion criteria.
# 3.	Displaying eligibility results and department validation.
class Employee:
    min_exp=5
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def eligiable_promotion(self):
        if self.experience>=Employee.min_exp:
            return "Eligible for promotion"
        return "Not Eligible for promotion"
    @classmethod
    def update_promotion(cls,new_exp):
        cls.min_exp=new_exp
    @staticmethod
    def is_valid(Dept):
        Employee.dept=["hr","r&d","development","hardware","manufacturing","marketing"]
        if Dept.lower() in Employee.dept:
            return "Valid"
        return "Invalid"
Ramesh=Employee("Ramesh",6,"Training")
Ratamma=Employee("Ratamma",2,"Development")
Arjun=Employee("Arjun",1,"R&D")
Arjun.update_promotion(2)
print(f"{Arjun.name}->")
print(f"{Arjun.eligiable_promotion()}")
print(f"{Arjun.is_valid(Arjun.department)} Department")
print(f"{Ramesh.name}->")
print(f"{Ramesh.eligiable_promotion()}")
print(f"{Ramesh.is_valid(Ramesh.department)} Department")
print(f"{Ratamma.name}->")
print(f"{Ratamma.eligiable_promotion()}")
print(f"{Ratamma.is_valid(Ratamma.department)} Department")
# my instance has name,department,experience,a button with behaviour to tell i'm eligiable to promotion and another buuton
# to change the promotion crieteria and small tool button to tell if the given department is valid or not