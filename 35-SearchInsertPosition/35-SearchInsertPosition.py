# Last updated: 9/17/2025, 6:09:20 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left + right)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        return left


        