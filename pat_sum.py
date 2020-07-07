# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        return self.find(root, 0, sum)
    
    def find(self, node: TreeNode, cur_sum, summ):
        if node is None:
            return
        if node.left is None and node.right is None:
            return cur_sum + node.val == summ
        else:
            return self.find(node.left, cur_sum + node.val, summ) or self.find(node.right, cur_sum + node.val, summ)
