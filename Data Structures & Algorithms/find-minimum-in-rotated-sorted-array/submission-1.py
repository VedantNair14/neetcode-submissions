class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Step 1: Initialize the binary search pointers
        l = 0
        r = len(nums) - 1

        # Step 2: Loop until the boundaries meet
        while l < r:
            mid = l + ((r - l) // 2)

            # Step 3: Compare the middle element to the rightmost element
            if nums[mid] > nums[r]:
                # If the middle value is GREATER than the right value, 
                # it means the left-to-middle portion is normally sorted,
                # and the sudden drop (minimum value) MUST lie to the right of 'mid'.
                l = mid + 1
            else:
                # If the middle value is LESS than or EQUAL to the right value,
                # it means the middle-to-right portion is normally sorted.
                # The minimum value could be 'mid' itself, or it lies to the left.
                r = mid

        # Step 4: When the loop ends, 'l' and 'r' will converge on the minimum element
        return nums[l]