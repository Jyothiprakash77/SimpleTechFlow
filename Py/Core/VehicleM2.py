#M2
# Q6. Design a class Vehicle that:
# •	Keeps a record of service charge rate common to all vehicles.
# •	Each vehicle has a model, kilometers_run, and service history.
# •	Has a function to calculate service charge based on km and rate.
# •	Provides a method to update the service rate for all vehicles.
# •	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
# Demonstrate:
# 1.	Creating vehicles with different km and models.
# 2.	Updating the service rate.
# 3.	Showing charges and eligibility checks.
class Vehicle:
    service_rate=25
    def __init__(self,model,kilometers_run):
        self.model=model
        self.kilometers_run=kilometers_run
        self.service_history=[]
    def service_charge(self):
        return Vehicle.service_rate*self.kilometers_run
    @classmethod
    def change_servicerate(cls,new_rate):
        cls.service_rate=new_rate
    @staticmethod
    def service_eligible(model):
        if int(model[-2:len(model)]) <11:
            print("Not Eligible for service")
            return False
        else:
            print("Eligible for service")
            return True
Mahindra_Thar=Vehicle("Mahindra Thar22",700)
Ferari_SF90=Vehicle("Ferari_SF9025",500)
BMW_suv=Vehicle("BMW_suv10",1400)
Vehicle.service_rate=900
if BMW_suv.service_eligible(BMW_suv.model):
    print(BMW_suv.service_charge())


