# A Neon number is a special type of number where the sum of the digits of its square
# is equal to the number itself.(Nine)
n=int(input())
sq=n**2
s=0
while sq>0:
    r=sq%10
    s+=r
    sq//=10
if s==n:
    print(f"{s} is Neon number")
else:
    print(f"{n} is not a Neon number")