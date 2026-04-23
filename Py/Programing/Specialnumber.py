# A Special Number is a number where the sum of the factorials of its digits
# is equal to the number itself.
n=int(input())
def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac
temp=n
s=0
while temp>0:
    r=temp%10
    fac=factorial(r)
    s+=fac
    temp//=10
if s==n:
    print(f"{s} is special number")
else:
    print(f"{n} is not special number")