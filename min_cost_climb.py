def minCostClimbingStairs( cost: List[int]) -> int:
    dp = [0 for _ in range(len(cost))]
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost) - 1):
        dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
    return min(dp[-2], dp[-3] + cost[-1])
