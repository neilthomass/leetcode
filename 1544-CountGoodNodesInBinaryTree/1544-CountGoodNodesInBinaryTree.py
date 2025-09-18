# Last updated: 9/17/2025, 6:07:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        def search(root,num):

            count = 1

            if not root:
                return 0

            if root.val < num:
                return search(root.right,num) + search(root.left,num)

            if root.left:
                count += search(root.left,root.val)

            if root.right:
                count += search(root.right,root.val)

            return count

            
             
        return 1 + search(root.left,root.val) + search(root.right,root.val)



        