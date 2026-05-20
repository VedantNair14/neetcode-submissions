class Solution:
    def trap(self, height: list[int]) -> int:
        # If the array is empty or has fewer than 3 bars, no water can be trapped
        if not height:
            return 0

        # Step 1: Initialize two pointers at opposite ends
        l, r = 0, len(height) - 1
        
        # Step 2: Track the tallest bars seen so far from left and right
        leftMax, rightMax = height[l], height[r]
        total_water = 0

        # Step 3: Move pointers inward until they meet
        while l < r:
            # We always process the side with the smaller max boundary
            if leftMax < rightMax:
                l += 1  # Move left pointer right
                # Update the maximum boundary from the left
                leftMax = max(leftMax, height[l])
                # Add trapped water at current position to the total
                total_water += leftMax - height[l]
            else:
                r -= 1  # Move right pointer left
                # Update the maximum boundary from the right
                rightMax = max(rightMax, height[r])
                # Add trapped water at current position to the total
                total_water += rightMax - height[r]

        return total_water