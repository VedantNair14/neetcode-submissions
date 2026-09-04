class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            # Base Case 1: Successfully matched all letters of the word!
            if i == len(word):
                return True

            # Base Case 2: Out of bounds, character mismatch, or already visited ("#")
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != word[i]):
                return False

            # Step 1: Temporarily mark this cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Step 2: Explore all 4 adjacent directions (Down, Up, Right, Left)
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            # Step 3: Backtrack - restore the original character
            board[r][c] = temp

            return found

        # Try starting DFS from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False