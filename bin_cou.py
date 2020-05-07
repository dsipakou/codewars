# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._d = {}
    
    def dfs(self, root: TreeNode, depth: int, parent=None): 
        if root is not None:
            self._d[root.val] = [depth, parent]
            self.dfs(root.left, depth + 1, root.val)
            self.dfs(root.right, depth + 1, root.val)
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.dfs(root, 0)
        if self._d[x][0] == self._d[y][0] and self._d[x][1] != self._d[y][1]:
            return True
        return False
