def decodeWays(s):

    noOfWays = [0] + [1] * len(s)

    for i in range(1, len(s) + 1):
        if 0 < int(s[i - 1 : i + 1]) <= 26:
            noOfWays[i] += noOfWays[i - 1]
        else:
            noOfWays[i] = noOfWays[i - 1]
    
    return noOfWays[-1]

print(decodeWays("2101"))