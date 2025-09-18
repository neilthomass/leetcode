# Last updated: 9/17/2025, 6:08:39 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
        