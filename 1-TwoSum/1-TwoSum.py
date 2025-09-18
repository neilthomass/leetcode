"""
Problem: 1-TwoSum
Last updated: 9/18/2025, 1:05:25 PM
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Runtime: 4 ms (Beats 41.62%)
Memory: 18.8 MB (Beats 62.03%)
Language: python3
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
             return [i, pair_idx[target - num]]
            pair_idx[num] = i
        


        