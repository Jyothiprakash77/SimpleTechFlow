# • Create class Employee with an instance method salary(). Create class
# Manager(Employee) that overrides salary() and adds an incentive. Demonstrate
# both outputs.
class Employee:
    def __init__(self):
        self.Salary = 50000
    def salary(self):
        print(self.Salary)
class Manager(Employee):
    def salary(self):
        print(self.Salary+60000)
M1=Manager()
M1.salary()
