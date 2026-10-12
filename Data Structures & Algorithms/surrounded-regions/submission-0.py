class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int):
            # Base Case: Out of bounds or not an 'O'
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return

            # Mark this border-connected 'O' as safe ('T')
            board[r][c] = "T"

            # Check all 4 adjacent neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Run DFS from 'O's located on the borders
        # Check Top and Bottom rows
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        # Check Left and Right columns
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        # Step 2: Traverse the entire board to capture trapped 'O's and restore safe 'T's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    # Truly surrounded by 'X's -> Capture it!
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    # Border-connected -> Restore back to 'O'
                    board[r][c] = "O"