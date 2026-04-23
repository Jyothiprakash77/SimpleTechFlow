# 1. Write a custom iterator that prints numbers from 1 to N.
class Natural:
    def __init__(self,end):
        self.num=0
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        self.num=self.num+1
        if self.num>self.end:
            raise StopIteration
        return self.num
Natural_numbers=Natural(50)
for i in Natural_numbers:
    print(i,end=" ")