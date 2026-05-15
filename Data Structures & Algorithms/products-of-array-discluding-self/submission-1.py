class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s
        res = [1] * (len(nums))

        # First Pass: Calculate Prefix Products
        # 'prefix' keeps track of the product of all numbers to the left
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix      # Store current prefix in result
            prefix *= nums[i]    # Update prefix for the next element

        # Second Pass: Calculate Postfix Products
        # 'postfix' keeps track of the product of all numbers to the right
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # Moving backwards
            res[i] *= postfix    # Multiply existing prefix by the current postfix
            postfix *= nums[i]   # Update postfix for the next element (moving left)

        return res    