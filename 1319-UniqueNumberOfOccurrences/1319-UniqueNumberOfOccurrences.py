# Last updated: 9/17/2025, 6:07:57 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for item in arr:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        
        return len(d.values()) == len(set(d.values()))
        