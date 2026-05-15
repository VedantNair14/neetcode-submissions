class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Create a new string with only alphanumeric characters in lowercase
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str += char.lower()
        
        # Step 2: Compare the cleaned string with its reverse
        # [::-1] is a Python trick that reverses a string
        return new_str == new_str[::-1]