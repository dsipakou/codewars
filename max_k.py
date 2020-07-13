def maxProfitWithKTransactions(prices, k):
    if not len(prices):
		return 0
	
    dp = [[0 for i in prices] for j in range(k + 1)]
    for i in range(1, k + 1):
        output = float('-inf')
        for j in range(1, len(prices)):
            output = max(output, dp[i - 1][j - 1] - prices[j - 1])
            dp[i][j] = max(dp[i][j - 1], output + prices[j])
    return dp[-1][-1]
