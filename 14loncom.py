class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        if not len(strs):
            return output
        i = 0
        fin = False
        while not fin:
            if i >= len(strs[0]):
                break
            curr = strs[0][i]
            for w in strs:
                if i >= len(w) or w[i] != curr:
                    fin = True
                    break
            if not fin:
                output += curr
            else:
                break
            i += 1
        return output
