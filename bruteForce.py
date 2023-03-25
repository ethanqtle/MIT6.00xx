def maxVal(toConsider, avail):
    """Assumes toConsider a list of items,
                avail a weight
       Returns a tuple of the total value of a
                solution to 0/1 knapsack problem and
                the items of that solution
                """
    if toConsider == [] or avail == 0:
        return (0, ())
    elif toConsider[0].getWeight() > avail:
        return maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            return (withVal, withToTake + (nextItem,))
        else:
            return (withoutVal, withoutToTake)
# in Python try implement this function
#def maxVal(toConsider, avail):


