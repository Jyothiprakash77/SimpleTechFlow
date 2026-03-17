# Q7. Create a class Employee with:
# •	instance attributes: name, base_salary
# •	class variable: bonus_rate = 0.1
# •	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# •	class method: update_bonus(cls, new_rate) → updates bonus for all employees
# •	static method: is_valid_salary(sal) → checks if salary > 0
# Create two employees, show final salaries, update bonus rate, and show again.
class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.Name=name
        self.base_salary=base_salary
    def final_salary(self):
        self.base_salary=int(self.base_salary+(self.base_salary*self.bonus_rate))
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(salary):
        return salary>0
Mugesh=Employee("Mugesh",10000)
Kuresh=Employee("Kuresh",15000)
Mugesh.update_bonus(0.5)
print(Mugesh.base_salary)
Mugesh.final_salary()
print(Mugesh.base_salary)
print(Kuresh.base_salary)
Kuresh.final_salary()
print(Kuresh.base_salary)