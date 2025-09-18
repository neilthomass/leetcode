# Last updated: 9/17/2025, 6:09:19 PM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        if n == 0:
            return 1
        
        result = 1
        while n:
            if n % 2 == 1:
                result *= x
            x *= x 
            n //= 2
        
        return result



            

        