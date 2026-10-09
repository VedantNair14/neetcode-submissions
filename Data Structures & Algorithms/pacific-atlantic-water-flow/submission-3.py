class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r: int, c: int, visited: set, prev_height: int):
            # Base Case: Stop if out of bounds, already visited, or height is lower than previous (cannot flow uphill)
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                (r, c) in visited or 
                heights[r][c] < prev_height):
                return

            visited.add((r, c))

            # Explore all 4 adjacent neighbors (Down, Up, Right, Left)
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Step 1: Run DFS from Top row (Pacific) and Bottom row (Atlantic)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])               # Top row (Pacific)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # Bottom row (Atlantic)

        # Step 2: Run DFS from Left col (Pacific) and Right col (Atlantic)
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])               # Left column (Pacific)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # Right column (Atlantic)

        # Step 3: Find coordinates that can reach BOTH oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res