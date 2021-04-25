class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        output = ''
        i = len(s)
        while i > 0:
            if output:
                output = '-' + output
            output = s[max(0, i - k): i] + output
            i = i - k
        return output
