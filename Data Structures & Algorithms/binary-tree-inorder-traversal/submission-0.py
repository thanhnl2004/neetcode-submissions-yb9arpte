# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inOrder(node, lst):
            if node:
                inOrder(node.left, lst)
                lst.append(node.val)
                inOrder(node.right, lst)
        inOrder(root, res)
        return res

        