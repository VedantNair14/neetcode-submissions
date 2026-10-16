from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list for the undirected graph
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        components = 0

        # Step 2: DFS to explore all nodes in the same component
        def dfs(node: int):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        # Step 3: Iterate through all nodes 0 to n - 1
        for i in range(n):
            if i not in visited:
                components += 1
                visited.add(i)
                dfs(i)

        return components