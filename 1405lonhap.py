class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        output = ''
        count = {'a': 0, 'b': 0, 'c': 0}
        while a != 0 and b != 0 and c != 0:
            max_str = max(a, b, c)
            if a == max_str:
                output += 'a'
                a -= 1
                count['a'] += 1
            elif b == max_str:
                output += 'b'
                b -= 1
                count['b'] += 1
            else:
                output += 'c'
                c -= 1
                count['c'] += 1
        return output
