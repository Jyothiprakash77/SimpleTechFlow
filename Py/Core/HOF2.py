#iterables must equal to parameters
#mutables won't change address after updation
#in membership operator takes the element and checks the each of the target
from functools import reduce

# 1. Explain the difference between map(), filter(), and reduce() in Python.
# • What does each function return?
# • When should you prefer lambda functions over normal functions?

# 2. Given two lists:
# a = [1, 2, 3, 4] b = [10, 20, 30, 40]
# Use map() with a lambda to create a new list containing the sum of corresponding
# elements.
# What happens if the lists are of unequal length?
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
l=list(map(lambda x,y:x+y,a,b))
#print(l)
#-if unequal list is given then the result will be the lowest length in the given of both
# 3. Given a list:
# nums = [12, 15, 7, 18, 20, 21, 25]
# Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
# 5 but NOT divisible by both.
# Explain how the logical condition works
nums = [12, 15, 7, 18, 20, 21, 25]
l=list(filter(lambda x:(not x%3) ^ (not x%5),nums))
#it operates wholely on the actual number to get actuall true or false lets use not operator
#print(l)
# 4. Given a list:
# nums = [1, 2, 3, 4]
# Use reduce() with a lambda to compute the sum, but start with an initial value
# of 10.
# Explain how the initial value affects the reduction process.
num = [1, 2, 3, 4]
num1=reduce(lambda x,y:x+y,num,100)
#reduce has initial value that is the 3rd variable which added with first element of the given list
print(num1)
