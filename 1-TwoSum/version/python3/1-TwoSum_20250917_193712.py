"""
Problem: 1-TwoSum
Last updated: 9/17/2025, 7:37:12 PM
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Runtime: 3 ms
Memory: 19.02 MB
Language: python3
"""

# Solution Notes: How bruh

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
             return [i, pair_idx[target - num]]
            pair_idx[num] = i


