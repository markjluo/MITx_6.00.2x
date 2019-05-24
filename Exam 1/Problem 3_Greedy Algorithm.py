def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to.
               L, list of unique positive integers sorted in descending order.
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    total = 0
    a = s
    for i in L:
        m = a//i
        multipliers.append(m)
        a -= m*i
    for j in range(len(L)):
        total += L[j]*multipliers[j]
    if total == s:
        return sum(multipliers)
    else:
        return 'no solution'

L = [6, 4, 3, 2]
s = 200
print(greedySum(L, s))