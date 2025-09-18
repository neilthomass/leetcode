# Last updated: 9/17/2025, 6:08:18 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in s:
            while True:
                if i == len(t):
                    return False
                if t[i] == char:
                    i += 1
                    break
                i += 1
    
            
        return True

        