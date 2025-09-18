# Last updated: 9/17/2025, 6:09:32 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        shortest = min(strs,key=len)
        for i in range (len(shortest)):
            if all([shortest[i] == item[i] for item in strs]):
                s += shortest[i]
            else:
                return s
        return s
        