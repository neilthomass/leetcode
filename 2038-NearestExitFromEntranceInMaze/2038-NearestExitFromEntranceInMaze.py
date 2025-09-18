# Last updated: 9/17/2025, 6:07:44 PM
from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], e: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        q = deque([(e[0], e[1], 0)])
        maze[e[0]][e[1]] = "+"

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            i, j, d = q.popleft()
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == ".":
                    if (ni == 0 or ni == n - 1 or nj == 0 or nj == m - 1):
                        return d + 1
                    maze[ni][nj] = "+"
                    q.append((ni, nj, d + 1))
        return -1