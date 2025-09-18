# Last updated: 9/17/2025, 6:07:33 PM
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [0] * 26
        upper = [0] * 26
        count = 0
 
        for char in word:
            if char >= 'a' and char <= 'z':
                lower[ord(char) - ord('a')] = 1
            else:
                upper[ord(char) - ord('A')] = 1
        
        for i in range(26):
            if lower[i] == 1 and upper[i] == 1:
                count += 1
        return count

