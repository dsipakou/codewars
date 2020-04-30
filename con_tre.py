# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for i in preorder[1:]:
            node = root
            in_node = TreeNode(i)
            while node:
                if i > node.val:
                    if node.right is None:
                        node.right = in_node
                        break
                    else:
                        node = node.right
                else:
                    if node.left is None:
                        node.left = in_node
                        break
                    else:
                        node = node.left
        return root
