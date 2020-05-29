class Solution:
    def countBits(self, num: int) -> List[int]:
        output = [0]
        if num == 0:
            return output
        for i in range(1, num + 1):
            if i == 1:
                output.append(1)
            else:
                output.append(output[i // 2] + output[i % 2])
        return output
