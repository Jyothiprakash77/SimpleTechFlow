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
#Use map() with a lambda to add 5 to every element of the following nested
#list [[1, 2], [3, 4], [5, 6]]
L6=[[1, 2], [3, 4], [5, 6]]
k=list(map(lambda x:x+[5],L6))
#print(k)

#Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
#filter() to keep only the keys whose values are greater than 50.
def rem(dic):
        if d[dic]>50:
            return True
        return False

d = {"apple": 100, "banana": 40, "cherry": 150}
D1=list(filter(rem,d))
#print(D1)
#Use functools.reduce() with a lambda to find the largest number from a given
#list Dynamically.
#L1=list(map(int,input("Enter numbers: \n").split(" ")))
#print(L1)
#Use map() on a string to convert each character into its ASCII value
#(using ord()). Print the result list.
string="hang"
S=list(map(lambda x:ord(x),string))
#print(S)

# 6.  Use filter() to remove all vowels from a string and print the final string.
s="hi I'm Jyothi"
S1=list(filter(lambda x:x not in "aeiouAEIOU",s))
print(S1)
#Use reduce() to concatenate a list of characters into a single string.
#Example input: ['P', 'y', 't', 'h', 'o', 'n'].
St=['P', 'y', 't', 'h', 'o', 'n']
St=str(reduce(lambda a,b:a+b,St))
#print(St)

#Given a list of integers, use map() with id() to print the memory address
#of each element.
#Example: [10, 350, 10, 350, 20] — explain why some addresses repeat
Ex=[10, 350, 10, 350, 20, 89, 67]
def address(x):
    return f"{x}->{id(x)}"
L9=list(map(address,Ex))
#print(L9)

#Explain the difference between:
#map(str, [1, 2, 3])
#map(lambda x: str(x), [1, 2, 3])
#Which one is faster and why?

# Given a list of numbers:
#[5, 10, 15, 20, 25, 30]
#Perform the following in a single pipeline:
#• Use map() to square each number
#• Use filter() to keep only numbers divisible by 5
#• Use reduce() to calculate the sum of remaining number
L8=[5, 10, 15, 20, 25, 30]
sum=reduce(lambda a,b:a+b,list(filter(lambda x:True if x%5==0 else False,list(map(lambda x:x**2,L8)))))
print(sum)
