# A Harshad number (or Niven number) is a number that is divisible by the sum of its own digits.
#
# The name comes from the Sanskrit words Harsha (joy) and da (give), meaning "Joy-giver."
# In mathematics, it’s like the number is "happy" because it can be perfectly divided by its own parts.
n=int(input())
s=0
temp=n
while temp>0:
    r=temp%10
    s+=r
    temp//=10
if n%s==0:
    print(f"{n} is harshad number")
else:
    print(f"{n} is not a harshad number")
