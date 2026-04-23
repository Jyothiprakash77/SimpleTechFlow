# A Perfect Number is a positive integer that is exactly equal to the sum of its proper divisors
# (all its factors excluding the number itself).
#
# In the world of mathematics, these numbers are considered "perfect" because they represent
# a rare balance between a number and its constituent parts.
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")