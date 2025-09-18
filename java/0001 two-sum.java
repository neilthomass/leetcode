/**
 * Last updated: 9/18/2025, 2:03:25 PM
 * URL: https://leetcode.com/problems/two-sum/
 * Runtime: 2 ms (Beats 98.89%)
 * Memory: 44.9 MB (Beats 65.12%)
 * Language: java
 */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> pairIdx = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (pairIdx.containsKey(target - num)) {
                return new int[] { i, pairIdx.get(target - num) };
            }
            pairIdx.put(num, i);
        }

        return new int[] {};        
    }
}