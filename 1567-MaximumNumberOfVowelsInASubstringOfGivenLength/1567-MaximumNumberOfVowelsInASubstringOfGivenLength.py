# Last updated: 9/17/2025, 6:07:52 PM
class Solution:
    
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        v = sum([s[i] in vowels for i in range(k)])
        mv = v
        for i in range(k,len(s)):
            if s[i-k] in vowels: v -= 1
            if s[i] in vowels: v += 1
            mv = max(mv,v)

        return mv


        

        