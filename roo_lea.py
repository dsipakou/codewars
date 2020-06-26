# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.all_nums = []
        
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.dfs(root, "")
        return sum(int(a) for a in self.all_nums)
    
    def dfs(self, node, prefix):
        current_val = prefix + str(node.val)
        if node.left is None and node.right is None:
            self.all_nums.append(current_val)
            return
        if node.left is not None:
            self.dfs(node.left, current_val)
        if node.right is not None:
            self.dfs(node.right, current_val)
