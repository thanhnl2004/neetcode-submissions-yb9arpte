# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        values = []
        def dfs(node, values):
            if node:
                dfs(node.left, values)
                values.append(node.val)
                dfs(node.right, values)
        
        dfs(root, values)
        if len(values) == 1: return True
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]: return False
        
        return True
        