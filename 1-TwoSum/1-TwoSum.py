"""
Problem: 1-TwoSum
Last updated: 9/18/2025, 12:54:27 PM
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Runtime: 0 ms (Beats 100%)
Memory: 19.2 MB (Beats 10.32%)
Language: python3
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
             return [i, pair_idx[target - num]]
            pair_idx[num] = i
        


        