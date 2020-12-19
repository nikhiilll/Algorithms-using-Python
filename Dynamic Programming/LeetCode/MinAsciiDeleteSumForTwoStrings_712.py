def minAsciiDeleteSumForTwoStrings(s1, s2):

    l1, l2 = len(s1) + 1, len(s2) + 1

    matrix = [[0 for i in range(l2)] for j in range(l1)]
    
    for i in range(1, l2):
        matrix[0][i] = matrix[0][i - 1] + ord(s2[i - 1])
    
    for i in range(1, l1):
        matrix[i][0] = matrix[i - 1][0] + ord(s1[i - 1])

    for i in range(1, l1):
        for j in range(1, l2):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j] + ord(s1[i - 1]), matrix[i][j - 1] + ord(s2[j - 1]))
    
    return matrix[-1][-1]

print(minAsciiDeleteSumForTwoStrings("delete", "leet"))