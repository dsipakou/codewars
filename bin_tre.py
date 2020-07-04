# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        pivot = len(nums) // 2
        root = TreeNode(nums[pivot])
        root.left = self.ins(root, nums, 0, pivot - 1)
        root.right = self.ins(root, nums, pivot + 1, len(nums) - 1)
        return root
        
    def ins(self, node, nums, left, right):
        if left > right:
            return
        pivot = (right - left) // 2 + left
        tmp = TreeNode(nums[pivot])
        tmp.left = self.ins(tmp, nums, left, pivot - 1)
        tmp.right = self.ins(tmp, nums, pivot + 1, right)
        return tmp
