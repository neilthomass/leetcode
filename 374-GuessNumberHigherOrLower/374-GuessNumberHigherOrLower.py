# Last updated: 9/17/2025, 6:08:20 PM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        upper = float("inf")
        lower = 0
        g = guess(n)
        while g:
            if g < 0:
                upper = n
            else:
                lower = n
            n = lower + (upper - lower)//2
            g = guess(n)
        return n