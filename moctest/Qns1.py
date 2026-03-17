L1=[1,2,6,5,2,3,8,9,12]
from functools import reduce
n=reduce(lambda x,y:x+y,list(filter(lambda x:x%7==0,list(map(lambda x:x**2,L1)))),0)
print(n)