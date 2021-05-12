class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == '../':
                if len(stack) > 0:
                    stack.pop()
            elif log == './':
                continue
            else:
                stack.append('1')
        return len(stack)
