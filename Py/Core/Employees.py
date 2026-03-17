class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
Dipak=Employee("Dipak")
print(Dipak.name,Dipak.company_name)
Dipak.change_company("Power_RV")
print(Dipak.name,Dipak.company_name)