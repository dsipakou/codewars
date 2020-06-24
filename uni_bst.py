class Solution:
    def numTrees(self, n: int) -> int:
        print(n)
        G = [0]*(n+1)
        G[0], G[1] = 1, 1
        print(G)

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
                print(G)

        return G[n]
