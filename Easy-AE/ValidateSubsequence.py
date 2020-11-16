def isValidSubsequence(array, sequence):
    """
    TC: O(n), SC: O(m)
    """
    stack = sequence[::-1]

    for num in array:
        if stack and stack[-1] == num:
            stack.pop()
        
    return (len(stack) == 0)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))