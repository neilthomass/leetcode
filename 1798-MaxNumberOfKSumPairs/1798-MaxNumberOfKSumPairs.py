# Last updated: 9/17/2025, 6:07:46 PM
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        i, j = 0, len(nums)-1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == k:
                count += 1
                i += 1
                j -= 1
            elif sum < k:
                i += 1
            else:
                j -= 1
        return count 

