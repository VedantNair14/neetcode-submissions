import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0, 0)]  # (edge_cost, point_index)
        visited = set()
        total_cost = 0

        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)

            # Skip nodes that have already joined our spanning tree
            if u in visited:
                continue

            # Include node u in the tree
            visited.add(u)
            total_cost += cost

            # Calculate Manhattan distance from node u to all other unvisited nodes
            x1, y1 = points[u]
            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, v))

        return total_cost  