def counting(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
n=int(input())
count=counting(n)
if(count%2==0):
    div=10**(count//2)
    p1=n//div
    p2=n%div
    if (p1+p2)**2 == n:
        print(f"{n} is tech number")
    else:
        print("Not a tech number")
else:
    print("Can't determine")
