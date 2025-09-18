# Last updated: 9/17/2025, 6:08:09 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        for i in range(len(nums)):
            right -= nums[i]
            if right == left:
                return i
            left += nums[i]
        return -1