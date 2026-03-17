def is_prime(n):
    fc=0
    if n==2:
        return True
    elif n==3:
        return True
    else:
        for i in range(2,n//2):
            if n%i==0:
                fc+=1
        if fc==0:
            return True
        return False
def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
    return rev
def is_palindrome(n):
    rev=0
    temp=n
    while n>0:
        r=n%10
        rev = (rev * 10) + r
        n = n // 10
    return rev==temp
n=int(input())
a=is_prime(n)
b=is_prime(reverse(n))
c=not(is_palindrome(n))
if a and b and c:
    print(f"{n} is Emirp number")
else:
    print(f"{n} is not a Emirp number")