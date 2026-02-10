from operator import truediv
def cube(a):
    return a**3
def divide7(n):
    if(n%7==0):
        return True
    return False
def multiply(a,b):
    return a*b
L1 = [11,12,13,14,15,16,17,18,19,20]
L7 = [67,98,33,24,56,87,3465,26]
L=list(map(cube, L1))
L=list(filter(divide7,L7))
from functools import reduce
L=(reduce(multiply,L1))
L=list(sorted(L7,key=cube,reverse=True))
print(L)