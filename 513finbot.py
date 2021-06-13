# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [[root]]
        while queue:
            current = queue.pop(0)
            left = current[0]
            level = []
            while current:
                node = current.pop(0)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                queue.append(level)
        return left.val
