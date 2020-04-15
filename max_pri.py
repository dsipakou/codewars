def max_profit(prices):
    output = float('-inf')
    for i in range(len(prices) - 1):
        output = max(max(prices[i + 1:]) - prices[i], output)
    return output