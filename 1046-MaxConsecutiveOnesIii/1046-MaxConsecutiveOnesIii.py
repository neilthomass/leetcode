# Last updated: 9/17/2025, 6:08:02 PM
class Solution:
    def longestOnes(self, nums, k):
        left, maxLength, zeroCount = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            
            maxLength = max(maxLength, i - left + 1)
        return maxLength