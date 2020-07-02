# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        output = []
        if not root:
            return output
        
        def dfs(node, level):
            if len(output) == level:
                output.append([])
                
            output[level].append(node.val)
            print(output)
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
                
        
        dfs(root, 0)
        return output[::-1]
