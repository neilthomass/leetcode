# Last updated: 9/17/2025, 6:07:58 PM
class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        
        