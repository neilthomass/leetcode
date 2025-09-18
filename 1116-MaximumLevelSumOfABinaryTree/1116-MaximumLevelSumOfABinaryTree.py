# Last updated: 9/17/2025, 6:08:00 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        sums = []

        while q:
            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sums.append(curr_sum)

        return sums.index(max(sums)) + 1 







        