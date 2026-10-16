class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node: int, prev: int) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n