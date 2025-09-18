# Last updated: 9/17/2025, 6:07:45 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(min(len(word1),len(word2))):
            ans += word1[i] + word2[i]
        return ans + word1[i+1:] + word2[i+1:]
            
        