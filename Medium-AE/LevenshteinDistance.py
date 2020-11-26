def levenshteinDistance(str1, str2):
    """
    TC: O(nm) | SC: O(nm)
    """
    edits = [[x for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]
    for y in range(len(str1) + 1):
        edits[y][0] = y
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i][j - 1], edits[i - 1][j - 1], edits[i - 1][j])
    
    return edits[-1][-1]
