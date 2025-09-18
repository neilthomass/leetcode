# Last updated: 9/17/2025, 6:07:39 PM
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            if s[i] == "*":
                ans.pop()
            else:
                ans.append(s[i])
        
        return "".join(ans)