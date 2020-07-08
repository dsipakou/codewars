def palindromePartitioningMinCuts(string):
    if len(string) == 1:
        return 0
    dp = [[None] * len(string) for _ in range(len(string))]
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j + 1] == string[i:j + 1][::-1]:
                dp[i][j] = True
            else:
                dp[i][j] = False
    output = [float('inf') for _ in range(len(string))]
    for i in range(len(string)):
        if dp[0][i]:
            output[i] = 0
        else:
            output[i] = output[i - 1] + 1
            for j in range(1, len(string)):
                if dp[j][i] and output[j - 1] + 1 < output[i]:
                    output[i] = output[j - 1] + 1
    return output[-1]
