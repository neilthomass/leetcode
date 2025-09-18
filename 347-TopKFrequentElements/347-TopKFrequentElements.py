# Last updated: 9/17/2025, 6:08:21 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:

            d[n] += 1

        valToNums = defaultdict(list)

        for key, v in d.items():
            valToNums[v].append(key)
        
        res = []
        for v in sorted(valToNums.keys(),reverse = True):
            res.extend(valToNums[v])
        return res[:k]