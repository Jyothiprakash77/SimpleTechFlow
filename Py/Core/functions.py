def is_even(n):
    if n%2==0:
        return True
    return False
def is_odd(n):
    if n%2==0:
        return False
    return True
def altereven(n):
    if n%2==0:
        global position+=1
        if position%2==1:
            return True
    return False
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
count=0
position=0
for i in range(n1,n2+1):
    if is_even(i):
        if count != 1:
            print(", ", end="")
        print(i,end="")
    count+=1
