class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # Stores pairs of (index, height)

        for i, h in enumerate(heights):
            start = i
            # If current height is SHORTER than the top of stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area: height * (current_index - original_start_index)
                maxArea = max(maxArea, height * (i - index))
                # The new bar we are adding can actually "start" from the popped index
                start = index
            
            stack.append((start, h))

        # After the loop, process any bars remaining in the stack
        # These bars could extend all the way to the end of the histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea