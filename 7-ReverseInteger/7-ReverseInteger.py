# Last updated: 9/17/2025, 6:09:37 PM
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        
        if x < 0:
            x = -x
            i = -1
        else:
            i = 1

        while x:
            res = res * 10 + x % 10
            x //= 10
        
        
        return res * i if -2**31 < res < 2**31 - 1 else 0

        