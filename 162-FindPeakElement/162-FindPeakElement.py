# Last updated: 9/17/2025, 6:08:34 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] > nums[mid+1]:
                j = mid
            else:
                i = mid + 1
        return i
        