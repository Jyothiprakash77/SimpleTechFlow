def Digits(n):
    reverse=0
    temp=n
    while temp>0:
        r=temp%10
        reverse=reverse*10+r
        temp//=10
    temp=reverse
    while temp>0:
        r=temp%10
        yield r
        temp//=10
for i in Digits(23980):
    print(i,end=" ")