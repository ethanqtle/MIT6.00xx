# 

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    def count_elem(L):
        countDict = dict()
        for elem in L:
            if elem in countDict:
                countDict[elem] += 1
            else:
                countDict[elem] = 1
        return countDict

    # Check if the two lists have the same length
    if len(L1) != len(L2):
        return False
    elif len(L1) == 0 and len(L2) == 0:
        return (None, None, None)

    # Create Counter objects for each list to count the occurrences of each element
    count_L1 = count_elem(L1)
    count_L2 = count_elem(L2)
    
    # Check if the two Counter objects are equal
    if count_L1 != count_L2:
        return False
    
    # Find the element occurring most frequently and its count
    most_common_element, count = None, 0
    for elem in count_L1:
        if count_L1[elem] > count:
            most_common_element, count = elem, count_L1[elem]
    
    # Determine the type of the most common element
    
    element_type = type(most_common_element)
    
    return (most_common_element, count, element_type)

# Test
print(is_list_permutation([1, 2, 3], [3, 2, 1]))
print(is_list_permutation([1, 2, 3], [3, 2, 1, 1]))
print(is_list_permutation([1, 2, 3], [3, 2, 2]))

# if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
# if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] 
# then is_list_permutation returns (1, 3, <class 'int'>)
# because the integer 1 occurs the most, 3 times, and 
# the type of 1 is an integer (note that the third element in the tuple is not a string).
print(is_list_permutation([], []))
print(is_list_permutation(['a', 'a', 'b'], ['a', 'b']))
print(is_list_permutation([1, 'b', 1, 'c', 'c', 1], ['c', 1, 'b', 1, 1, 'c']))


