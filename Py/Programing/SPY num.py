n=int(input())
sum=0
mul=1
num=n
while n>0:
    r=n%10
    sum+=r
    mul*=r
    n=n//10
if mul == sum :
    print(f"{num} is SPY number")
else:
    print(f"{num} is not a spy number")