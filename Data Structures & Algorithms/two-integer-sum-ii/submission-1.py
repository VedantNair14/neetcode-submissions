class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Initialize two pointers
        # 'l' starts at the beginning (smallest number)
        # 'r' starts at the end (largest number)
        l, r = 0, len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target:
                # If sum is too large, we need a smaller number.
                # Since the array is sorted, moving 'r' to the left 
                # gives us a smaller value.
                r -= 1
            elif currentSum < target:
                # If sum is too small, we need a larger number.
                # Moving 'l' to the right gives us a larger value.
                l += 1
            else:
                # We found the target! 
                # The problem asks for 1-indexed results.
                return [l + 1, r + 1]  