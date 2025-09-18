# Last updated: 9/17/2025, 6:07:54 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = []
        m = max(candies)
        for candy in candies:
            if candy + extraCandies >= m:
                a.append(True)
            else:
                a.append(False)
        return a
        