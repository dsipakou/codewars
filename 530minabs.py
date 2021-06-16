# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        output = []
        queue = [root]
        while queue:
            current = queue.pop(0)
            output.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        output.sort()
        min_out = output[1] - output[0]
        for i in range(len(output) - 1):
            min_out = min(min_out, output[i + 1] - output[i])
        return min_out
