class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Step 1: Initialize the result array filled with 0s
        # If a day never finds a warmer temperature, it naturally stays 0
        res = [0] * len(temperatures)
        
        # This stack will store pairs of [temperature, index]
        stack = [] 

        # Step 2: Loop through every day with its index and temperature
        for i, t in enumerate(temperatures):
            # Step 3: While the stack isn't empty AND today's temp is warmer
            # than the temperature sitting at the top of the stack
            while stack and t > stack[-1][0]:
                # Pop the colder day out of the waiting room
                stack_t, stack_i = stack.pop()
                
                # Calculate the distance (number of days waited)
                res[stack_i] = i - stack_i
                
            # Step 4: Push the current day's [temperature, index] onto the stack
            stack.append([t, i])
            
        return res