# Last updated: 9/17/2025, 6:09:25 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode(0)
        p = ans

        while any(lists):
            lists.sort(key=lambda x: x.val if x else float("inf"))   

            ans.next = ListNode(lists[0].val)
            ans = ans.next
            lists[0] = lists[0].next
           
        return p.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        items = []
        for l in lists:
            while l:
                items.append(l.val)
                l = l.next
        items.sort()
        
        answer = None
        while items:
            answer = ListNode(items.pop(),answer)
        
        return answer

        
        
        
            
            