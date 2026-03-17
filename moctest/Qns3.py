class TimeTraveler:
    registry=[]
    def __init__(self,codename,origin_year,destination_year):
        self.codename=codename
        self.origin_year=origin_year
        self.destination_year=destination_year
        TimeTraveler.registry.append(self)
    @classmethod
    def show_registry(cls):
        total=len(cls.registry)
        print(f"Total time Travelers-{total}")
        for i in cls.registry:
            print(i.codename)
    @staticmethod
    def year_status(year):
        if year == 2026:
            return "Present"
        elif year>2026:
            return "Future"
        else:
            return "Past"
T1=TimeTraveler("NS667",2026,1809)
T2=TimeTraveler("NS235",3010,2003)
T3=TimeTraveler("NS846",2035,8900)
TimeTraveler.show_registry()
# print(T1.year_status(T1.origin_year))
# print(T2.year_status(T2.origin_year))
# print(T3.year_status(T3.origin_year))