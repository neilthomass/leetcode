# Last updated: 9/17/2025, 6:08:30 PM
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def price(num):
            if num < 0:
                return 0
            return nums[num] + max(price(num-3),price(num-2))


        return max(price(n -1),price(n - 2))

        
        