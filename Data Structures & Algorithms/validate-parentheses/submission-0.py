class Solution:
    def isValid(self, s: str) -> bool:
        # Step 1: Create an empty list to act as our stack
        stack = []
        
        # Step 2: Create a map (dictionary) matching close brackets to open brackets
        # This makes checking for a match clean and simple
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # Step 3: Iterate through every character in the string
        for char in s:
            # If the character is a closing bracket
            if char in closeToOpen:
                # Check if the stack is not empty AND the top element matches
                # In Python, stack[-1] looks at the top (last) element without removing it
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop() # Successfully matched! Remove from stack
                else:
                    return False # Mismatch or closed bracket with no open pair
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # Step 4: If the stack is completely empty, all brackets were matched perfectly
        return True if not stack else False  