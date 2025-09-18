# Last updated: 9/17/2025, 6:08:35 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        l = [item for item in s.split(" ")[::-1] if item.strip()]
        return " ".join(l)
        