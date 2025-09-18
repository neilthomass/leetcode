# Last updated: 9/17/2025, 6:08:32 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        canidate = 0

        for num in nums:
            if count == 0:
                canidate = num
                count += 1
            elif num == canidate:
                count += 1
            else:
                count -= 1
        
        return canidate
        