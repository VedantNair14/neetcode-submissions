class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i):
            # Base Case: We've made a decision for every element in nums
            if i >= len(nums):
                # Append a copy of the current subset
                res.append(subset.copy())
                return

            # Decision 1: INCLUDE nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack: Remove nums[i] to explore the second branch
            subset.pop()

            # Decision 2: EXCLUDE nums[i]
            dfs(i + 1)

        # Start recursion from index 0
        dfs(0)
        return res