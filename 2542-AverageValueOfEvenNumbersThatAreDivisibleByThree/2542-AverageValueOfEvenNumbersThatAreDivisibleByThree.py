# Last updated: 9/17/2025, 6:07:37 PM
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        i = 0
        c = 0
        for n in nums:
            if n % 3 == 0 and n % 2 == 0:
                c += n
                i += 1

        if c == 0:
            return 0
        return c//i

