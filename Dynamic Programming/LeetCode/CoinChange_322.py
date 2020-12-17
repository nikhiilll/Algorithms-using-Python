def coinChange(coins, amount):
    """
    TC: O(n) | SC: O(n)
    """
    minCoins = [float("inf") for _ in range(amount + 1)]
    minCoins[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)
            else:
                minCoins[i] = float("inf")
    
    return minCoins[-1] if minCoins[-1] != float("inf") else -1

print(coinChange([1, 2, 5, 7], 18))
                