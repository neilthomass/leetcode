# Last updated: 9/17/2025, 6:07:41 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []

        while head:
            values.append(head.val)
            head = head.next


        n = len(values)
        m = 0

        for i in range(n//2):

            m = max(m, values[i] + values[n-1-i])

        return m

        