# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._count = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.print_node(root, k).val
        
    def print_node(self, node, k):
        if node is None:
            return None
        
        left = self.print_node(node.left, k)
        
        if left is not None:
            return left
        
        self._count += 1
        if self._count == k:
            return node
        
        return self.print_node(node.right, k)
