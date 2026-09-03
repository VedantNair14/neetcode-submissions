class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open_n: int, closed_n: int):
            # Base Case: We placed all n opening and n closing parentheses
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            # Decision 1: Can we add an open parenthesis?
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()  # Backtrack

            # Decision 2: Can we add a close parenthesis?
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()  # Backtrack

        # Start with 0 open and 0 closed parentheses
        backtrack(0, 0)
        return res