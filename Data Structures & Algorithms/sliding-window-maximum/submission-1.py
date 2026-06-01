from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        # q will store indices of elements in our window
        q = deque() 
        
        l = 0
        for r in range(len(nums)):
            # Step 1: Remove smaller elements from the back of the queue
            # because they can never be the maximum of the current or future windows
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # Add the current element's index to the back of the queue
            q.append(r)
            
            # Step 2: Remove the left index from the front of the queue 
            # if it has fallen outside the current window boundaries
            if l > q[0]:
                q.popleft()
                
            # Step 3: Once our window reaches size 'k', record the maximum
            # The maximum element is always at index q[0] (the front of the queue)
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1 # Slide the left boundary forward
                
        return res