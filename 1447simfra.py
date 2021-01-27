class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        output = []
        for i in range(2,n + 1):
            output.append(f"1/{i}")
        for i in range(2, n + 1):
            for j in range(i + 1, n + 1):
                if (j % i == 0 and j <= n) or self.gdc(i, j):
                    continue
                output.append(f'{i}/{j}')
        return output
    
    def gdc(self, n1, n2):
        for i in range(2, min(n1, n2) + 1):
            if n1 % i == 0 and n2 % i == 0:
                return True
        return False
