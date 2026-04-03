# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        heightLeft = self.height(root.left)
        heightRight = self.height(root.right)
        isCurrentBalanced = abs(heightLeft - heightRight) <= 1
        return isCurrentBalanced and self.isBalanced(root.left) and self.isBalanced(root.right) 



    def height(self, root: Optional[TreeNode]):
        if not root:
            return -1
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
        
        