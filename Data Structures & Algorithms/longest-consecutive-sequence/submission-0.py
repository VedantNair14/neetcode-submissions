class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Step 1: Put all numbers into a set for O(1) lookups
        numSet = set(nums)
        longest = 0

        # Step 2: Iterate through every number in the set
        for n in numSet:
            # Step 3: Check if this number is the START of a sequence
            # (Check if the number just before it exists)
            if (n - 1) not in numSet:
                length = 1
                
                # Step 4: While the NEXT number exists, keep counting
                while (n + length) in numSet:
                    length += 1
                
                # Update the record for the longest sequence found so far
                longest = max(length, longest)
                
        return longest