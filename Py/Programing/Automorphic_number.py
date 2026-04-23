# An Automorphic number (also known as a circular number) is a special type of number
# where the square of the number ends with the same digits as the number itself.
n=int(input())
sq=n**2
count=0
temp=n
while temp>0:
    count+=1
    temp//=10
n1=sq%(10**count)
if n1==n:
    print("Automorphic number")
else:
    print("Not a automorphic number")
