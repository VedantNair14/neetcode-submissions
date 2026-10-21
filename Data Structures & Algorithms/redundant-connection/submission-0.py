from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Nodes are labeled 1 to n
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        # Find the root representative with path compression
        def find(node: int) -> int:
            curr = node
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]  # Path compression
                curr = parent[curr]
            return curr

        # Union by rank: returns False if nodes are ALREADY connected (cycle!)
        def union(n1: int, n2: int) -> bool:
            p1, p2 = find(n1), find(n2)

            # If both nodes share the same root, adding this edge forms a cycle
            if p1 == p2:
                return False

            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Process each edge in order
        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []