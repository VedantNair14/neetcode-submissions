class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []
        
        # Step 1: Sort to group duplicate numbers together
        nums.sort()

        def dfs(i: int):
            # Base Case: When we've considered all elements
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Decision 1: INCLUDE nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()  # Backtrack

            # Decision 2: EXCLUDE nums[i]
            # Skip all duplicate copies of nums[i] so we don't branch redundantly
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            # Recurse on the next distinct number
            dfs(i + 1)

        dfs(0)
        return res