# Last updated: 9/17/2025, 6:08:27 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        curr = head
        
        while curr and curr.next:
            prev, curr.next, curr = curr, prev, curr.next
        
        
        curr.next = prev

        return curr


        