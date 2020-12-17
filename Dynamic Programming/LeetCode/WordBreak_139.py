def wordBreak(s, wordDict):

    canBreak = [False for _ in range(len(s) + 1)]
    canBreak[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if canBreak[j] and s[j : i] in wordDict:
                canBreak[i] = True
                break

    return canBreak[-1]
            