# Last updated: 9/17/2025, 6:08:43 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if not root:
            return l

        l.extend(self.inorderTraversal(root.left))

        l.append(root.val)

        l.extend(self.inorderTraversal(root.right))


        return l
        