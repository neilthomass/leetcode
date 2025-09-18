# Last updated: 9/17/2025, 6:08:13 PM
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()
        max_len = 0
        
        for i in range(len(nums)):
            if i not in seen:
                start = i
                count = 0
                while nums[start] not in seen:
                    seen.add(nums[start])
                    start = nums[start]
                    count += 1
                max_len = max(max_len, count)
        return max_len