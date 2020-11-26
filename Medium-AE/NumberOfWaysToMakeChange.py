def numberOfWaysToMakeChange(n, denoms):
    """
    TC: O(nd) | SC: O(n)
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in denoms:
    	for i in range(1, n + 1):
            if coin <= i:
                dp[i] += dp[i - coin]
    
    return dp[n]
