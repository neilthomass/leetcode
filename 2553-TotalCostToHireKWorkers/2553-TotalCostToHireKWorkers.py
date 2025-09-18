# Last updated: 9/17/2025, 6:07:37 PM
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        i = 0
        j = len(costs) - 1
        pq1 = []
        pq2 = []

        ans = 0
        
        for _ in range(k):
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1,costs[i])
                i += 1
            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2,costs[j])
                j -= 1

            t1 = pq1[0] if pq1 else float("inf")
            t2 = pq2[0] if pq2 else float("inf")

            if t1 <= t2:
                ans += t1
                heapq.heappop(pq1)
            else:
                ans += t2
                heapq.heappop(pq2)
        return ans
            
                


        