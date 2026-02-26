class Person:
    no_ofPhones=0
    def __init__(self,name,age,Phone_no):
        self.name=name
        self.age=age
        self.Phone_no=Phone_no
        if Phone_no>0:
            Person.no_ofPhones+=1
p1=Person("Madhava",21,9867908345)
print(p1.no_ofPhones)