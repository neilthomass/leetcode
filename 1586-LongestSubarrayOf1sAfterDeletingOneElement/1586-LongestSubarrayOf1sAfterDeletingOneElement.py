# Last updated: 9/17/2025, 6:07:50 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j,maxc,c = 0,0,1

        for i in range(len(nums)):
            if nums[i] != 1:
                c -= 1
            
            while c < 0:
                if nums[j] != 1:
                    c += 1
                j += 1


            maxc = max(maxc,i-j)
        return maxc
        