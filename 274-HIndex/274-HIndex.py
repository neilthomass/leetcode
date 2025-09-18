# Last updated: 9/17/2025, 6:08:25 PM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i, v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0
