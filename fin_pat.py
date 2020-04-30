# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root.val != arr[0]:
            return False
        else:
            return self.dfs(root, 0, arr)
    
    def dfs(self, node, pos, arr):
        if node is None or node.val != arr[pos]:
            return False
        if pos == len(arr) - 1:
            if node.left or node.right:
                return False
            return True
        else:
            return self.dfs(node.left, pos + 1, arr) or self.dfs(node.right, pos + 1, arr)
