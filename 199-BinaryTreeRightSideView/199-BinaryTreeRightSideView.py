# Last updated: 9/17/2025, 6:08:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque()
        q.append(root)
        while q:

            right = None

            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)

            if right:
                ans.append(right.val)

        return ans




        
        
        