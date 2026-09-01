class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        curr = []
        used = [False] * len(nums)

        def backtrack():
            # Base Case: When the current permutation has all elements
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            # Try placing every available number at the current position
            for i in range(len(nums)):
                if not used[i]:
                    # 1. Choose nums[i]
                    used[i] = True
                    curr.append(nums[i])

                    # 2. Explore deeper paths
                    backtrack()

                    # 3. Backtrack: Undo the choice
                    curr.pop()
                    used[i] = False

        backtrack()
        return res