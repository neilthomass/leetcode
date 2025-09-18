# Last updated: 9/17/2025, 6:09:21 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[c] = nums[i]
                c += 1
        return c
        