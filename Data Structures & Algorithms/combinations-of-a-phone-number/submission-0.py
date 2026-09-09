class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge Case: If input is empty, return an empty list immediately
        if not digits:
            return []

        # Step 1: Mapping digits to keypad letters
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        # Step 2: Backtracking helper function
        def backtrack(i: int, cur_str: str):
            # Base Case: When we've picked a letter for every digit
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return

            # Explore all possible letters for the current digit digits[i]
            for c in digit_to_char[digits[i]]:
                backtrack(i + 1, cur_str + c)

        # Start recursion from the first digit (index 0) with an empty string
        backtrack(0, "")
        return res