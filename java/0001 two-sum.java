/**
 * Last updated: 9/18/2025, 8:38:32 PM
 * URL: https://leetcode.com/problems/two-sum/
 * Runtime: 2 ms (Beats 98.89%)
 * Memory: 45.1 MB (Beats 31.42%)
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