# Last updated: 9/17/2025, 6:09:15 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and c > 0:
                return c
            elif s[i] != " ":
                c += 1
        return c
            
            

   
        