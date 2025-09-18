# Last updated: 9/17/2025, 6:09:22 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        index = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[index] = nums[i]
                seen.add(nums[i])
                index += 1
        return index
        