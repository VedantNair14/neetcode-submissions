class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Step 1: Initialize two pointers at the boundaries of the array
        l = 0
        r = len(nums) - 1

        # Step 2: Loop until the boundaries cross each other
        while l <= r:
            # Step 3: Find the middle index
            # Using integer division (//) to get a whole number
            mid = l + ((r - l) // 2)

            # Step 4: Compare the middle element to our target
            if nums[mid] == target:
                return mid # Found it! Return its index.
                
            elif nums[mid] < target:
                # If the middle value is too small, the target must be on the right side.
                # Narrow the search window by shifting the left boundary past 'mid'.
                l = mid + 1
                
            else:
                # If the middle value is too big, the target must be on the left side.
                # Narrow the search window by shifting the right boundary before 'mid'.
                r = mid - 1

        # Step 5: If the loop ends without finding the target, it doesn't exist
        return -1