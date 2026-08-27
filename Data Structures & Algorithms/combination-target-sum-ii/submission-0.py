class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        # Step 1: Sort candidates to group duplicates together and enable early stopping
        candidates.sort()

        def backtrack(start: int, cur: list[int], remaining: int):
            # Base Case 1: Found a valid combination
            if remaining == 0:
                res.append(cur.copy())
                return

            # Explore all possible next numbers starting from 'start'
            for i in range(start, len(candidates)):
                # Early Pruning: If the current number exceeds remaining, all numbers after it will too
                if candidates[i] > remaining:
                    break

                # Duplicate Pruning: Skip identical values at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose candidates[i]
                cur.append(candidates[i])

                # Recurse: Move to i + 1 since each element can only be used ONCE
                backtrack(i + 1, cur, remaining - candidates[i])

                # Backtrack: Undo the choice
                cur.pop()

        # Start recursion from index 0 with empty combination and full target
        backtrack(0, [], target)
        return res