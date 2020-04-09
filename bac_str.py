class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        index = 0
        S = list(S)
        for i, v in enumerate(S):
            if v != '#':
                S[index] = v
                index += 1
            elif index > 0:
                index -= 1
        S = S[:index]
        T = list(T)
        index = 0
        for i, v in enumerate(T):
            if v != '#':
                T[index] = v
                index += 1
            elif index > 0:
                index -= 1
        T = T[:index]
        return S == T