# Last updated: 9/17/2025, 6:07:54 PM
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            res.insert(index[i],nums[i])
        return res
        