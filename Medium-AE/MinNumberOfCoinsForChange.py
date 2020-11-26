def minNumberOfCoinsForChange(n, denoms):

    ways = [float("inf") for _ in range(n + 1)]
    ways[0] = 0

    for i in range(1, n + 1):
        for coin in denoms:
            if coin <= i:
                ways[i] = min(ways[i], ways[i - coin] + 1)

    return ways[n] if ways[n] != float("inf") else -1


