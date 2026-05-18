class Solution:
    def maxArea(self, heights: list[int]) -> int:
        # Step 1: Initialize two pointers at the extreme ends
        l = 0
        r = len(heights) - 1
        max_area = 0

        # Step 2: Loop until the pointers meet
        while l < r:
            # Calculate the width between pointers
            width = r - l
            
            # Find the limiting height (the shorter bar)
            current_height = min(heights[l], heights[r])
            
            # Calculate current area and update max_area if it's larger
            current_area = width * current_height
            max_area = max(max_area, current_area)

            # Step 3: Crucial Decision - Move the pointer pointing to the shorter bar
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area 