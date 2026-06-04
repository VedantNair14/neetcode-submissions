class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for t in tokens:
            # Check if the token is an operator
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "-":
                # Order matters for subtraction!
                # The first pop is the second number (b), the second pop is the first number (a)
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif t == "/":
                # Order matters for division!
                b = stack.pop()
                a = stack.pop()
                # Use int() to handle truncation toward zero as requested
                stack.append(int(a / b))
            else:
                # If it's a number, convert the string to an integer and push it
                stack.append(int(t))
                
        # The final remaining element in the stack is the total result
        return stack[0]