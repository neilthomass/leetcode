# Last updated: 9/17/2025, 6:07:55 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.pathLength = 0

        def dfs(node, l, s):
            if node:
                self.pathLength = max(self.pathLength, s)
                if l:
                    dfs(node.left, False, s + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, s + 1)

        dfs(root, True, 0)
        return self.pathLength

    

    


        