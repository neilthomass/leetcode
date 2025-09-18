# Last updated: 9/17/2025, 6:09:26 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = ListNode(0)
        p = ans

        while list1 or list2:
            
            if not list1:
                ans.next = list2
                break
            
            if not list2:
                ans.next = list1
                break

            if list1.val <= list2.val:

                ans.next = ListNode(list1.val)
                list1 = list1.next
                ans = ans.next
            else:

                ans.next = ListNode(list2.val)
                list2 = list2.next
                ans = ans.next
            
        
        return p.next



        