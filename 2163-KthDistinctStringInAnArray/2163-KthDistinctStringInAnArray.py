# Last updated: 9/17/2025, 6:07:43 PM
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = defaultdict(int)

        for s in arr:
            d[s] += 1
        
        count = 0
        for key in d:
            if d[key] == 1:
                count += 1
            if count == k:
                return key
        return ""

