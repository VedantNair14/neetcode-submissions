class MinStack:

    def __init__(self):
        # Initialize two empty lists acting as our parallel stacks
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Determine the current minimum value to push onto the minStack
        # If minStack is not empty, compare the new val with the top of minStack
        if self.minStack:
            current_min = min(val, self.minStack[-1])
        else:
            current_min = val
            
        self.minStack.append(current_min)

    def pop(self) -> None:
        # Since both stacks stay perfectly synced, pop from both simultaneously
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the last item added to the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the last item added to the minStack (guaranteed to be the minimum)
        return self.minStack[-1]