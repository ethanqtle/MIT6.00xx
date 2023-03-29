#!/usr/bin/env python

# We are not certain that McDonald’s knows about Diophantine equations 
# (actually we doubt that they do), but they use them! McDonald’s sells
# Chicken McNuggets in packages of 6, 9 or 20 McNuggets. Thus, 
# it is possible, for example, to buy exactly 15 McNuggets (with one
# package of 6 and a second package of 9), but it is not possible to
# buy exactly 16 nuggets, since no non negative integer combination
# of 6’s, 9’s and 20’s adds up to 16. To determine if it is possible
# to buy exactly n McNuggets, one has to solve a Diophantine equation:
# find non-negative integer values of a, b, and c, such that 
# 6a + 9b + 20c = n

# Declare array sol as 151 None to store results
sol = [None] * 151

# Prefer large box (20) to small box (6)
# iterate through all possible values of c, b, and a
for c in range(0, 151):
    for b in range(0, 151):
        for a in range(0, 151):
            # if 6a + 9b + 20c = n, then set sol[n] to True
            n = 6*a + 9*b + 20*c
            # store (a, b, c) in sol[n] if n is less than 151
            if n < 151:
                sol[n] = (a, b, c)
            else:
                break
# print header
print("n", "sol[n] == (6a + 9b + 20c == n))")

# print out the results as line of n, sol[n]
# for n in range(1, 151):
#     print(n, sol[n])

# print for the range [50..66]
print("sol[50..65] == (6a + 9b + 20c == n)")
for n in range(50, 66):
    print(n, sol[n])
    
    
# Find the largest n that cannot be bought in exact quantity
for n in range(150, 0, -1):
    if sol[n] == None:
        print("The largest n that cannot be bought in exact quantity is", n)
        break

