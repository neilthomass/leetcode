# Last updated: 9/17/2025, 6:07:45 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        seen = set()
        left = 0
        currSum = 0
        m = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                currSum -= nums[left]
                seen.remove(nums[left])
                left += 1
            currSum += nums[right]
            seen.add(nums[right])
            m = max(m,currSum)
        return m
            

        