# Last updated: 9/17/2025, 6:07:41 PM
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.q = []
        self.curr = 1


        

    def popSmallest(self) -> int:
        if self.q:
            return heapq.heappop(self.q)
        self.curr += 1
        return self.curr - 1
        
        

    def addBack(self, num: int) -> None:
        if num not in self.q and num < self.curr:
            heapq.heappush(self.q, num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)