# Last updated: 9/17/2025, 6:08:11 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = sum(nums[0:k])
        maxs = m
        n = len(nums)
        for i in range(k,n):
            m = m + nums[i] - nums[i-k]
            maxs = max(maxs,m)
        return maxs/k

        