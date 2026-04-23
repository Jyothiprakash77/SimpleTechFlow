n=int(input())
count=1
a=0
b=1
while count<=n:
    if count==n:
        print(a)
    c=a+b
    a=b
    b=c
    count+=1