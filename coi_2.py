class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        output = [1]
        output.extend([0] * amount)
        print(output)
        for coin in coins:
            for i in range(coin, len(output)):
                output[i] += output[i - coin]
        return output[-1]
