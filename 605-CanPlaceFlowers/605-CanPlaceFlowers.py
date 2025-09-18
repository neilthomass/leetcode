# Last updated: 9/17/2025, 6:08:12 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        open = 0
        q = len(flowerbed)
        prev = True
        for i in range(q):
            if not flowerbed[i]:
                t = True
                if i - 1 >= 0:
                    if flowerbed[i-1]:
                        t = False
                
                if i + 1 < q:
                    if flowerbed[i+1]:
                        t = False
                if t and prev:
                    open += 1
                    prev = False
                else:
                    prev = True


        return open >= n
                
        

