"""
Last updated: 9/22/2025, 2:41:03 PM
URL: https://leetcode.com/problems/implement-trie-prefix-tree/
Runtime: 68 ms (Beats 19.86%)
Memory: 32.2 MB (Beats 41.25%)
Language: python3
"""

class Trie:

    def __init__(self):
        self.ch = {}
        self.end = False
        

    def insert(self, word: str) -> None:
        node = self
        for c in word:

            node = node.ch.setdefault(c, Trie())
        node.end = True


            

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            node = node.ch.get(c)
            if node is None:
                return False
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            node = node.ch.get(c)
            if node is None:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)