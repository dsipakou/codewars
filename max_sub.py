# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = float('-inf')
    
    def maxPathSum(self, root: TreeNode) -> int:
        left = self.getMax(root.left)
        right = self.getMax(root.right)
        val = root.val
        self.output = max(
            self.output,
            val,
            val+left+right,
            val+left,
            val+right
        )
        return self.output
    
    def getMax(self, node: TreeNode) -> int: 
        if node is None:
            return 0
        left = self.getMax(node.left)
        right = self.getMax(node.right)
        val = node.val
        cur_max = max(left+right+val, val, left+val, right+val)
        self.output = max(self.output, cur_max)
        return max(left+val, right+val, val)
