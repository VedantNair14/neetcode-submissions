class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Detect that a cycle exists and find an intersection point
        slow = nums[0]
        fast = nums[0]
        
        # We use a 'while True' because both slow and fast start at nums[0]
        while True:
            slow = nums[slow]          # Moves 1 step: slow = pointer
            fast = nums[nums[fast]]    # Moves 2 steps: fast = pointer to pointer
            if slow == fast:
                break
                
        # Phase 2: Find the entrance of the cycle (the duplicate number)
        slow2 = nums[0] # Start a new pointer at the beginning
        
        while slow != slow2:
            slow = nums[slow]   # Moves 1 step
            slow2 = nums[slow2] # Moves 1 step
            
        return slow # or slow2, since they are pointing to the exact same duplicate