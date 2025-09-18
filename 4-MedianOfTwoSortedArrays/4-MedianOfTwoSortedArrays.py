# Last updated: 9/17/2025, 6:09:39 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        n = len(l)
        mid = n//2
        if n%2:
            return l[mid]
        return (l[mid]+l[mid-1])/2

        