#class
class car:
    Company="naidu_drive"
    count=0
    def __init__(self):
        self.name='unknown'
        self.count+=1
SCORPIO=car()
BMW=car()
Ferrari=car()
SCORPIO.name="Scorpio"
SCORPIO.speed=798
BMW.name="BMW"
BMW.model="bmwi8"
Ferrari.name='F91'
print(SCORPIO.name,SCORPIO.Company  ,end=" ")
print(BMW.name,BMW.Company,end=" ")
print( Ferrari.name,Ferrari.Company,end="\n")
print(Ferrari.count)
print(car.count)