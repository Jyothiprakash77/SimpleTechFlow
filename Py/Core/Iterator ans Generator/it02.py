#2. Create an iterator that returns only even numbers from a given list
from functools import reduce
class Onlyeven:
    def __init__(self,l):
        self.c=0
        self.L=list(filter(lambda x:x%2==0,l))
    def __iter__(self):
        return self
    def __next__(self):
        self.c+=1
        if self.c>len(self.L):
            raise StopIteration
        return self.L[self.c-1]
l=[9898,964,3,7,5345,2]
E1=Onlyeven(l)
for i in E1:
    print(i,end=' ')