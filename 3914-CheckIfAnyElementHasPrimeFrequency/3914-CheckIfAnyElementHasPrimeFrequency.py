# Last updated: 9/17/2025, 6:07:30 PM
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1


        def is_prime(n):
            if not isinstance(n, int) or n < 2:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            for i in range(5, int(n**0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
        
        for v in d.values():
            if is_prime(v):
                return True
        return False

        
        


        