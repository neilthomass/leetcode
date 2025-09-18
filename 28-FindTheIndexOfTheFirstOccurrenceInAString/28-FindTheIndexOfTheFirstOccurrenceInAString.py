# Last updated: 9/17/2025, 6:09:21 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        l = []
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
        