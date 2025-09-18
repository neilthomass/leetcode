# Last updated: 9/17/2025, 6:08:38 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    visited = {}


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited = {}
        return self.clone(node)
    

    def clone(self, node):
        if not node:
            return
        if node.val in self.visited:
            return self.visited[node.val]
        n = Node(node.val)
        self.visited[node.val] = n
        n.neighbors = [self.clone(nei) for nei in node.neighbors]
        return n

        