class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int):
            # Base Case: Stop if out of bounds or if the cell is water ('0')
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                grid[r][c] == "0"):
                return

            # "Sink" the island cell so it is not visited again
            grid[r][c] = "0"

            # Visit all 4 neighbors: Down, Up, Right, Left
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Traverse every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # Discovered a new unvisited island
                    islands += 1
                    # Sink the entire connected landmass
                    dfs(r, c)

        return islands