class Employee:
    Bonus=10000
    def __init__(self,name,salary):
        if Employee.is_valid_salary(salary):
            self.name=name
            self.salary=salary
        else:
            print("Invalid Salary")
            return None
    def display_details(self):
        print(f"Name:{self.name} Salary:{self.salary}")
    @classmethod
    def update_bonus(cls,new_bonus):
        cls.Bonus=new_bonus
    @staticmethod
    def is_valid_salary(salary):
        if salary>100000:
            return False
        return True
class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def display_details(self):
        print(f"Name:{self.name} Salary:{self.salary} Department:{self.dept}")
E1=Employee("Rajesh",12300)
M1=Manager("Harish",95000,"HR")
E1.display_details()
M1.display_details()