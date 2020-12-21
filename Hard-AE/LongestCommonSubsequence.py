def longestCommonSubsequence(str1, str2):
    """
    TC: O(nm * min(n, m)) | SC: O(nm * min(n, m))
    """
    # lcs = [[[] for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    # for i in range(1, len(str1) + 1):
    #     for j in range(1, len(str2) + 1):

    #         if str1[i - 1] == str2[j - 1]:
    #             lcs[i][j] = lcs[i - 1][j - 1] + [str1[i - 1]]
    #         else:
    #             lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key = len)
    
    # return lcs[-1][-1]


    """
    TC: O(mn) | SC: O(mn)
    """
    lcs = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):

            if str1[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    
    return theLongestSequence(lcs, str1)

def theLongestSequence(lcs, str1):

    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1

    while i != 0 and j != 0:

        if lcs[i][j] == lcs[i - 1][j]:
            i -= 1
        elif lcs[i][j] == lcs[i][j - 1]:
            j -= 1
        else:
            sequence.append(str1[i - 1])
            i -= 1
            j -= 1
    
    return list(reversed(sequence))

print(longestCommonSubsequence("ZXVVYZW", "XKYKZPW"))