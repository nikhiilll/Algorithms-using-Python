def maximumLengthOfPairChain(pairs):

        
    pairs.sort()
        
    maxLength = [1 for _ in range(len(pairs))]
    maxLengthFound = float("-inf")

    for i in range(1, len(pairs)):
        for j in range(i):

            if pairs[j][1] < pairs[i][0]:
                maxLength[i] = max(maxLength[i], maxLength[j] + 1)
        maxLengthFound = max(maxLengthFound, maxLength[i])

    return maxLengthFound

print(maximumLengthOfPairChain([[1,2], [2,3], [3,4]]))