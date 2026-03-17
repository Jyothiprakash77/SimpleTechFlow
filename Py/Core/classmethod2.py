class Student:
    batch=6
    def __init__(self,name):
        self.Name=name
    def change_batch(self,newbatch):
        self.batch=newbatch
    @classmethod
    def change_batchname(cls,newbatch):
        cls.batch=newbatch

s1=Student("Rohit")
s1.change_batch(4)
#Student.change_batchname(7)
Student.change_batch(s1,9)
#why this
print(f"{s1.Name} and batch-{s1.batch}")
print(f"student batch-{Student.batch}")