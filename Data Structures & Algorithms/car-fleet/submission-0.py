class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Step 1: Pair each car's position with its speed
        # e.g., pairs = [[pos1, speed1], [pos2, speed2], ...]
        pairs = [[p, s] for p, s in zip(position, speed)]
        
        # Step 2: Sort the cars by position in descending order (closest to target first)
        pairs.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        
        # Step 3: Calculate the time for each car and check for fleets
        for p, s in pairs:
            # Time = (Distance to target) / Speed
            time = (target - p) / s
            stack.append(time)
            
            # If the current car takes less than or equal time compared to the car in front of it
            # it means this car will catch up and become part of that front car's fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Remove this faster car from the stack because it merges into the slower fleet ahead
                stack.pop()
                
        # The number of elements remaining in the stack is the total number of fleets
        return len(stack)    