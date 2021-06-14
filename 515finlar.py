# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [[root]]
        output = []
        while queue:
            current_level = queue.pop(0)
            cur_max = float('-inf')
            level = []
            for item in current_level:
                if item.left:
                    level.append(item.left)
                if item.right:
                    level.append(item.right)
                cur_max = max(cur_max, item.val)
            output.append(cur_max)
            if level:
                queue.append(level)
        return output
