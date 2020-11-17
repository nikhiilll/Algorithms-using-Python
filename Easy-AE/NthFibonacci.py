def getNthFib(n):
    
    if n == 0:
        return 0

    a, b = 0, 1

    for _ in range(n - 2):
        a, b = b, a + b
    
    return b

"""
TC: O(n) | SC: O(1)
"""

def getNthFib2(n):

    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib2(n - 1) + getNthFib2(n - 2)

def getNthFib3(n):

    fibNums = {0: 0, 1: 0, 2: 1}

    if n in fibNums:
        return fibNums[n]
    else:
        fibNums[n] = getNthFib3(n - 1) + getNthFib3(n - 2)
        return fibNums[n]
"""
TC: O(n), SC: O(n)
"""
print(getNthFib3(6))