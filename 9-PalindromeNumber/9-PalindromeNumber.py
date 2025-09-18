# Last updated: 9/17/2025, 6:09:35 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
        