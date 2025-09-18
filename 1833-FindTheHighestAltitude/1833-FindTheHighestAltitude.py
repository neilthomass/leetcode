# Last updated: 9/17/2025, 6:07:48 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        max_sum = 0
        for i in range(len(gain)):
            sum += gain[i]
            max_sum = max(max_sum,sum)
        return max_sum
        