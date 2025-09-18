# Last updated: 9/17/2025, 6:08:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, cur=0):
            if not node:
                return cur
            if not node.left and not node.right:
                return 2 * cur + node.val
            left = dfs(node.left, 2 * cur + node.val) if node.left else 0
            right = dfs(node.right, 2 * cur + node.val) if node.right else 0
            return left + right

        return dfs(root)

            
