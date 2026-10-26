import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Min-Heap stores tuples: (max_elevation_so_far, r, c)
        min_heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        # 4 possible directions to swim: Down, Up, Right, Left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            time, r, c = heapq.heappop(min_heap)

            # Reached bottom-right target
            if r == n - 1 and c == n - 1:
                return time

            # Check all 4 adjacent neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check bounds and make sure it has not been visited
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    # The time to step onto neighbor (nr, nc) is the maximum
                    # between the current path's bottleneck time and grid[nr][nc]
                    heapq.heappush(min_heap, (max(time, grid[nr][nc]), nr, nc))