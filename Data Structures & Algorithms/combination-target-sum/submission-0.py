class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, cur, total):
            # Base Case 1: Exact target matched!
            if total == target:
                res.append(cur.copy())
                return
            
            # Base Case 2: Exceeded target or no more numbers available
            if total > target or i >= len(nums):
                return

            # Decision 1: INCLUDE nums[i] (stay at index i to allow reuse)
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # Backtrack: Clean up the shared list
            cur.pop()

            # Decision 2: EXCLUDE nums[i] (move forward to i + 1)
            dfs(i + 1, cur, total)

        # Start search at index 0 with empty combination and total sum 0
        dfs(0, [], 0)
        return res