def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """

    if len(L) == 0:
        return float('NaN')
    lengths = [len(i) for i in L]
    mean = sum(lengths)/len(lengths)
    sum_sq = 0
    for l in lengths:
        sum_sq += (l-mean)**2
    std_dev = (sum_sq/(len(lengths)))**(1/2)
    return std_dev

L = []
print(stdDevOfLengths(L))