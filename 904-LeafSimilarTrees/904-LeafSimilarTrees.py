# Last updated: 9/17/2025, 6:08:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def leaves(root):
            l = ()

            if not root.left and not root.right:
                return (root.val,)

            if root.left:
                l += leaves(root.left)

            if root.right:
                l += leaves(root.right)

            return l
        
        return leaves(root1) == leaves(root2)
            
        