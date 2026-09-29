from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0

        # Step 1: Count fresh fruits and collect all initial rotten fruits into the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # Step 2: BFS wave-by-wave while there are rotten fruits to process AND fresh fruits remain
        while q and fresh > 0:
            # Process all fruits rotting at the current minute mark
            for _ in range(len(q)):
                r, c = q.popleft()

                # Explore 4 neighbors: Up, Down, Left, Right
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    # If neighbor is valid and is a fresh fruit
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2   # Infect the fruit to rotten
                        fresh -= 1         # One less fresh fruit remaining
                        q.append((nr, nc)) # It will infect others in the next minute

            # 1 minute has elapsed for this level of infection
            minutes += 1

        # Step 3: If no fresh fruits remain, return total minutes; otherwise impossible
        return minutes if fresh == 0 else -1     