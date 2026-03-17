class Student:
    Degree="B-tech"
    College_name="VVIT"
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
        self.place="NA"#if i give zip code it must give me the city name
        self.address="NA"
        self.registration_no="NA"
        if branch.lower() == "cse":
            self.fees = 190000
        elif branch.lower() == "eee":
            self.fees = 120000
        elif branch.lower() == "ece":
            self.fees = 100000
        else:
            self.fees = 100000
P_Pradeep = Student("Pradeep","CSE")
print(f"fees of {P_Pradeep.name} is {P_Pradeep.fees}")