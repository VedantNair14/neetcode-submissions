class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Step 1: Create Hash Sets to track seen numbers
        # We use dictionaries where the value is a 'set' to avoid duplicates
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # Key will be (r//3, c//3)

        # Step 2: Iterate through every cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == ".":
                    continue
                
                num = board[r][c]
                
                # Step 3: Check for duplicates in current Row, Column, or Square
                # Square index is calculated by dividing row/col by 3
                if (num in rows[r] or 
                    num in cols[c] or 
                    num in squares[(r // 3, c // 3)]):
                    return False
                
                # Step 4: If not a duplicate, add it to our tracking sets
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)

        # If we check the whole board without returning False, it's valid!
        return True