# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc

counts = 0
longest = ""
for i in range(len(s)):
    if i == 0:
        longest = s[i]
        counts = 1
    elif s[i] >= s[i-1]:
        counts += 1
        if counts > len(longest):
            longest = s[i-counts+1:i+1]
    else:
        counts = 1
print("Longest substring in alphabetical order is: " + longest)
