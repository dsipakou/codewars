class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
            elif len(stack) == 0:
                return False
            else:
                last_char = stack.pop()
                if ch != mapping.get(last_char):
                    return False
        return len(stack) == 0
