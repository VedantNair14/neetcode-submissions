class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        # Helper to check if a substring s[l:r+1] is a palindrome
        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start: int):
            # Base Case: We've partitioned the entire string
            if start >= len(s):
                res.append(part.copy())
                return

            # Try making a cut after every index from 'start' to the end
            for end in range(start, len(s)):
                # Only proceed if the chosen prefix is a palindrome
                if is_palindrome(start, end):
                    part.append(s[start : end + 1])   # Choose
                    dfs(end + 1)                      # Recurse
                    part.pop()                        # Backtrack

        dfs(0)
        return res