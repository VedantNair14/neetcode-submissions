class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        # Get the dimensions of the 2D matrix
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        # Step 1: Treat the matrix as a 1D array of length (ROWS * COLS)
        # Initialize binary search pointers at the virtual 1D boundaries
        l = 0
        r = (ROWS * COLS) - 1
        
        # Step 2: Perform standard binary search
        while l <= r:
            mid = l + ((r - l) // 2)
            
            # Step 3: Map the 1D 'mid' index back to 2D coordinates (row, col)
            row = mid // COLS
            col = mid % COLS
            
            # Fetch the actual value from the matrix
            mid_val = matrix[row][col]
            
            # Step 4: Core binary search comparison logic
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False