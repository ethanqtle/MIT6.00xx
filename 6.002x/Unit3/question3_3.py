def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    # Your code here
    if len(L) == 0:
        return float('NaN')
    else:
        sum = 0
        for i in L:
            sum += len(i)
        mean = float(sum)/len(L)
        sum = 0
        for i in L:
            sum += (len(i) - mean)**2
        return (sum/len(L))**0.5
    
    
def stdDevAndMean(L):
  """
  L: a list of numbers
  returns: a tuple of floats, the standard deviation and the mean of L
  """
  # Your code here
  if len(L) == 0:
    return (float('NaN'), float('NaN'))
  else:
    sum = 0
    for i in L:
      sum += i
    mean = float(sum)/len(L)
    sum = 0
    for i in L:
      sum += (i - mean)**2
    return ((sum/len(L))**0.5, mean)

