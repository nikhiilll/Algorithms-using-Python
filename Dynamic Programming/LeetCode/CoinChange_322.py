def coinChange(coins, amount):
    """
    TC: O(n) | SC: O(n)
    """
    minCoins = [float("inf") for _ in range(amount + 1)]
    minCoins[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)
            print(minCoins)
    
    return minCoins[-1] if minCoins[-1] != float("inf") else -1
    # noOfWays = [0 for _ in range(amount + 1)]
    # noOfWays[0] = 1

    # for coin in coins:    
    #     for i in range(coin, amount + 1):
    #         noOfWays[i] += noOfWays[i - coin]
    
    # return noOfWays[-1]

print(coinChange([1, 2, 3], 4))
                