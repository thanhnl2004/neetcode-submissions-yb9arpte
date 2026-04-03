# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif root and subRoot:
            isRootSameTree = self.isSameTree(root, subRoot)
            if not isRootSameTree:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            else:
                return True
        elif root and notSubRoot:
            return True
        else:
            return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q:
            if p.val != q.val: return False
            isSameLeft = self.isSameTree(p.left, q.left)
            isSameRight = self.isSameTree(p.right, q.right)
            return isSameLeft and isSameRight
        else: 
            return False