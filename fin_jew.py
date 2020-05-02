class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        template = [-1 for _ in range(len(J))]
        if len(J) > 1:
            left = 0
            right = 1
            while right < len(J):
                if J[right] == J[left]:
                    template[right] = left
                    left += 1
                    right += 1
                else:
                    if left > 0:
                        left = template[left - 1] + 1
                    else:
                        right += 1
        top = 0
        bottom = 0
        output = 0
        while top < len(S):
            if S[top] == J[bottom]:
                top += 1
                bottom += 1
                if bottom >= len(J):
                    output += 1
                    bottom = 0
            else:
                if bottom > 0:
                    bottom = template[bottom-1] + 1
                else:
                    top += 1
        return output