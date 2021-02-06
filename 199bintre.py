# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        output = []
        level = []
        bfs = [root]
        while len(bfs) > 0:
            current = bfs.pop(0)
            if current.left:
                level.append(current.left)
            if current.right:
                level.append(current.right)
            if len(bfs) == 0:
                output.append(current.val)
                bfs.extend(level)
                level = []
        return output
