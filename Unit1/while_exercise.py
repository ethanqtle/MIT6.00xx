# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:49:07 2023

@author: ethanle
"""
# n this problem you'll be given a chance to practice writing some while loops.

# 1. Convert the following into code that uses a while loop.

# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

n = 2
while (n <= 10):
    print(n)
    n += 2
print('Goodbye!')

# 2. Convert the following into code that uses a while loop.

# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print('Hello!')
n = 10
while n >= 2:
    print(n)
    n -= 2

end= 6
# 3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

# For problems such as these, do not include input statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.

# Hint: Don't Use A Variable Called 'sum'

total = 0
i = 1
while i <= end:
    total += i
    i += 1
print(total)