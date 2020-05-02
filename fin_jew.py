class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        template = set(s for s in J)
        answer = 0
        for ch in S:
            if ch in template:
                answer += 1
        return answer