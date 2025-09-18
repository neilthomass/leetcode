# Last updated: 9/17/2025, 6:08:22 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = []
        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                v.append(s[i])
        a = ""
        v.reverse()
        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                a += v[0]
                v = v[1:]
            else:
                a += s[i]
        return a
