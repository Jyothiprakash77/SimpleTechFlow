class Speedometer:
    def __call__(self,distance,Time1,Time2):
        self.D=distance
        self.T1=Time1
        self.T2=Time2
        self.S1=self.D/self.T1
        self.S2=self.D/self.T2
        return round((2*self.S1*self.S2)/(self.S1+self.S2),2)
    def __sub__(self,speed2):
        return round(self.Avgspeed+speed2.Avgspeed,2)
    def __mul__(self,speed2):
        return self.Avgspeed*speed2.Avgspeed
    def __truediv__(self,speed2):
        return self.Avgspeed//speed2.Avgspeed
    def __le__(self,speed2):
        return self.Avgspeed>=speed2.Avgspeed
school=Speedometer()
school.Avgspeed=school(200,2.5,4)
office=Speedometer()
office.Avgspeed=office(400,9,3)
print(office/school)
print(office.Avgspeed)
print(school.Avgspeed)
