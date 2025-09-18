# Last updated: 9/17/2025, 6:09:40 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        w = ""
        s = list(s)
        for i in range(len(s)):
            if s[i] in w:
                m = max(m,len(w))
                while s[i] in w:
                    w = w[1:]
            w += s[i]

        return max(m,len(w))

        