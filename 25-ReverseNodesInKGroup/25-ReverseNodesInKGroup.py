# Last updated: 9/17/2025, 6:09:23 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = ListNode(0)
        a = ans
        rev = None
        counter = 0
        r = ListNode(0)
        while head:
            if counter % k == 0:
                pointer = head
                for i in range(k-1):
                    if not pointer.next:
                        ans.next = head
                        return a.next
                    pointer = pointer.next
                        

            rev = ListNode(head.val,rev)
            counter += 1
            head = head.next
            
            if counter % k == 0:
                ans.next = rev
                rev = None

                while ans.next:
                    ans = ans.next
                
        
        
    

        return a.next

