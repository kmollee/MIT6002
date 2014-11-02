def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if (len(L) == 0):
        return float('NaN')

    # compute mean first
    sumVals = 0
    for s in L:
        sumVals += len(s)
    meanVals = sumVals / float(len(L))

    # compute variance (average squared deviation from mean)
    sumDevSquared = 0
    for s in L:
        sumDevSquared += (len(s) - meanVals) ** 2
    variance = sumDevSquared / float(len(L))

    # standard deviation is the square root of the variance
    stdDev = variance ** (.5)

    return stdDev


def stdDevOfLengths2(L):
    # using listcomps
    n = float(len(L))
    if (n == 0):
        return float('NaN')
    lengths = [len(s) for s in L]
    mean = sum(lengths) / n
    squaredDev = [(l - mean) ** 2 for l in lengths]
    variance = sum(squaredDev) / n
    return variance ** (.5)


def stdDev(X):
    # using a separate function for std dev from lecture video
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot / len(X)) ** 0.5


def stdDevOfLengths3(L):
    n = len(L)
    if (n == 0):
        return float('NaN')
    X = []
    for s in L:
        X.append(len(s))
    return stdDev(X)

if __name__ == '__main__':
    # Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.
    print(stdDevOfLengths(['a', 'z', 'p']))
    # Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'],
    # stdDevOfLengths(L) should return 1.8708.
    print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))
