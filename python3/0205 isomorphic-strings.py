"""
Last updated: 9/22/2025, 2:29:22 PM
URL: https://leetcode.com/problems/isomorphic-strings/
Runtime: 7 ms (Beats 56.23%)
Memory: 17.7 MB (Beats 95.82%)
Language: python3
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_index_s = {}
        char_index_t = {}

        for i in range(len(s)):
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i
            if t[i] not in char_index_t:
                char_index_t[t[i]] = i
            
            if char_index_s[s[i]] != char_index_t[t[i]]:
                return False

        return True