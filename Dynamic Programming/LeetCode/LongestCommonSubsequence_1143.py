def longestCommonSubsequence(text1, text2):
    """
    TC: O(m*n) | SC: O(m*n)
    """
    l1, l2 = len(text1) + 1, len(text2) + 1
    matrix = [[0 for i in range(l2)] for j in range(l1)]

    for i in range(1, l1):
        for j in range(1, l2):

            if text1[i - 1] == text2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])
    
    return matrix[-1][-1]

print(longestCommonSubsequence("abcdef", "def"))