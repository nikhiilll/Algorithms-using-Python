def longestPalindromicSubsequence(s):

    reversedS = s[::-1]

    if s == reversedS:
        return len(s)
        
    lcs = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(s) + 1):

            if s[i - 1] == reversedS[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
    
    return lcs[-1][-1]

print(longestPalindromicSubsequence("bbbab"))