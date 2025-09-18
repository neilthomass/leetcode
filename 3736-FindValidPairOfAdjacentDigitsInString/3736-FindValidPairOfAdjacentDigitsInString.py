# Last updated: 9/17/2025, 6:07:32 PM
class Solution:
    def findValidPair(self, s: str) -> str:
        d = defaultdict(int)
        for l in s:
            d[l] += 1
        for i in range(len(s) - 1):
            if int(s[i]) == d[s[i]] and int(s[i+1]) == d[s[i+1]] and s[i] != s[i+1]:
                return s[i:i+2]
        return ""
