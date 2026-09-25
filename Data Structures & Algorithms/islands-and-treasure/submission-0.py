from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647

        # Step 1: Collect coordinates of all treasure chests (cells with value 0)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Step 2: Multi-source BFS starting outward from all chests simultaneously
        while q:
            r, c = q.popleft()

            # Explore 4 cardinal directions: Up, Down, Left, Right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # Only proceed if neighbor is within bounds and is an unvisited land cell (INF)
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    # Shortest distance is current cell's distance + 1
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))