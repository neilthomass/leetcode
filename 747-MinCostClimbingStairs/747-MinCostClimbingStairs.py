# Last updated: 9/17/2025, 6:08:08 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        cost.append(0)

        @cache
        def price(num):
            if num < 0:
                return 0
            return cost[num] + min(price(num-1),price(num-2))

        return price(l)



