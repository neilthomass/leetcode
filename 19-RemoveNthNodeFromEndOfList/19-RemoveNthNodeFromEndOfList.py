# Last updated: 9/17/2025, 6:09:29 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        i = 0
        ans = head
        p1 = head

        while p1.next != None:
            i += 1
            p1 = p1.next

        if head.next == None or i+1-n == 0:
            return head.next

        for i in range(i+1-n):
            prev = head
            head = head.next
        
        prev.next = head.next
        return ans
        

        
        

        