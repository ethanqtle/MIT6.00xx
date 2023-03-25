# Python Final MIT 6.00.1x exam Problem 3
# 
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = 'aeiouAEIOU'
    for char in s:
        if char not in vowels:
            print(char, end='')
    print() # print a newline at the end

# Test
print_without_vowels('This is great!')


    
