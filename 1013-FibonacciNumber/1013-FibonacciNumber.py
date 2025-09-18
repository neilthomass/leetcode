# Last updated: 9/17/2025, 6:08:04 PM
class Solution:

    @cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a,b = b, a + b
        return b
        