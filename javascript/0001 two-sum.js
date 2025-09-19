/**
 * Last updated: 9/18/2025, 8:17:37 PM
 * URL: https://leetcode.com/problems/two-sum/
 * Runtime: 2 ms (Beats 98.89%)
 * Memory: 45.1 MB (Beats 31.42%)
 * Language: javascript
 */

// O(n) - One-pass Hash Table
var twoSum = function(nums, target) {
    let map = new Map;
    for (var i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (map.has(complement)) {
            return [map.get(complement), i]
        }
        map.set(nums[i], i);
    }
}