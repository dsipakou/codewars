 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self, root: TreeNode) -> int:
        if root == None:
            return 0
        heightLeft = self.getHeight(root.left)
        heightRight = self.getHeight(root.right)
        return 1 + max(heightLeft, heightRight)
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        heightLeft = self.getHeight(root.left)
        heightRight = self.getHeight(root.right)
        
        diameterLeft = self.diameterOfBinaryTree(root.left)
        diameterRight = self.diameterOfBinaryTree(root.right)
        
        return max((heightLeft + heightRight), max(diameterLeft, diameterRight))