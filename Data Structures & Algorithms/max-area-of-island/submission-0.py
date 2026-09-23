class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            # Base Case: Out of bounds or current cell is water (0)
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                grid[r][c] == 0):
                return 0

            # "Sink" the land cell to mark it as visited
            grid[r][c] = 0

            # 1 (for the current cell) + sum of areas from all 4 directions
            return (1 + 
                    dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))

        # Scan the entire grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area