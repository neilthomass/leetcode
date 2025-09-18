# Last updated: 9/17/2025, 6:09:39 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        def expand(s,i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
            return s[i+1:j]

        for i in range(len(s)):
            ans = max(expand(s,i,i),expand(s,i,i+1),ans,key=len)
        return ans

