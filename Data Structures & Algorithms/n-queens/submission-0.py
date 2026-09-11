class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []
        # Initialize an empty n x n chessboard with dots
        board = [["."] * n for _ in range(n)]

        def backtrack(r: int):
            # Base Case: All n queens successfully placed row by row
            if r == n:
                # Convert the matrix of characters into the required list of strings
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Try placing a queen in every column of current row r
            for c in range(n):
                # If column or either diagonal is under attack, skip this cell
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # 1. Place the queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # 2. Recurse to the next row
                backtrack(r + 1)

                # 3. Backtrack: Remove the queen and clear attack sets
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        # Start placement from row 0
        backtrack(0)
        return res