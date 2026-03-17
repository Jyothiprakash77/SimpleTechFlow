class Student:
    batch=6
    def __init__(self,name):
        self.Name=name
    def change_batch(self,newbatch):
    #Everytime i call this won't get execute call will execute,this is time pass here
        self.batch=newbatch
    @classmethod
    def change_batch(cls,newbatch):
        cls.batch=newbatch

s1=Student("Rohit")
s1.change_batch(4)
#Student.change_batch(9)
print(f"{s1.Name} and batch-{s1.batch}")
print(f"student batch-{Student.batch}")