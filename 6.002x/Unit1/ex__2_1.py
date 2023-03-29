import random

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'
          
def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]
          
def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Get the length of the input list
    N = len(items)

    # Generate all possible trinary sequences of length N
    # Each item is in bag1 if trinary digit is 1
    # bag2 if digit is 2
    # none if digit is 0
    for i in range(3**N):
        bag1 = []
        bag2 = []
        iVal = i
        for j in range(N):
            # Use the jth trinary digit of i as a flag to determine whether item j is in bag1 or bag2
            if iVal % 3 == 1:
                bag1.append(items[j])
            elif iVal % 3 == 2:
                bag2.append(items[j])
            iVal = iVal // 3
            if iVal == 0:
                break
        yield (bag1, bag2)

# create combinations of items from a list counting in base 3
# for example, if the list is [1, 2, 3], then the combinations are
# [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 3, 1], [1, 3, 2], [1, 3, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 1], [2, 2, 2], [2, 2, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 2, 1], [3, 2, 2], [3, 2, 3], [3, 3, 1], [3, 3, 2], [3, 3, 3]

# create a list of all possible combinations of items in a list using itertools.product

# Get the length of the input list
    N = len(items)

    # Generate all possible trinary sequences of length N
    # Each item is in bag1 if trinary digit is 1
    # bag2 if digit is 2
    # none if digit is 0

def yieldAllCombos_itertools(items):
    """
    Generates all combinations of N items into two bags, whereby each 
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as 
    a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    # using itertools.product
    for combo in itertools.product([0, 1, 2], repeat=N):
        bag1 = []
        bag2 = []
        for i in range(len(combo)):
            if combo[i] == 1:
                bag1.append(items[i])
            elif combo[i] == 2:
                bag2.append(items[i])
        yield (bag1, bag2)
    