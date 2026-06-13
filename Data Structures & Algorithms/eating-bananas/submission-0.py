import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Step 1: Define the range for our binary search.
        # The minimum speed is 1 banana per hour.
        # The maximum speed is the largest pile size (eating one whole pile per hour).
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            
            # Step 2: Calculate total hours needed with speed 'k'
            total_time = 0
            for p in piles:
                # math.ceil(p / k) calculates hours for a pile, 
                # rounding up because Koko stays for the full hour.
                total_time += math.ceil(p / k)

            # Step 3: Check if this speed is slow enough or too fast
            if total_time <= h:
                # If we finished on time, this is a possible answer.
                # Try a smaller speed to find the absolute minimum.
                res = k
                r = k - 1
            else:
                # If it took too long, we must eat faster.
                l = k + 1
        
        return res