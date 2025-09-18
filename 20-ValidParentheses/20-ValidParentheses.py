# Last updated: 9/17/2025, 6:09:27 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")":"(","}":"{","]":"["}
        for c in s:
            if c in d.values():
                stack.append(c)
            elif not stack or stack and d[c] != stack.pop():
                return False
            
        return not stack