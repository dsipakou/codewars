# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode, level=1) -> int:
        if root is None:
            return 0
        depth = self.find_depth(root, 0)
        if depth == 0:
            return 1
        left, right = 0, 2**depth - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, depth, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return (2**depth - 1) + left
        
    def exists(self, idx, depth, node):
        left, right = 0, 2**depth - 1
        for _ in range(depth):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
        
    def find_depth(self, node, depth):
        if node.left is not None:
            return self.find_depth(node.left, depth + 1)
        return depth
        
