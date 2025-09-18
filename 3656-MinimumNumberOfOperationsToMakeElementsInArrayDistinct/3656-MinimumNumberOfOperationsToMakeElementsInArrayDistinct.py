# Last updated: 9/17/2025, 6:07:31 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        while nums:
            if len(nums) == len(set(nums)):
                break
            else:
                nums = nums[3:]
                c += 1
        return c