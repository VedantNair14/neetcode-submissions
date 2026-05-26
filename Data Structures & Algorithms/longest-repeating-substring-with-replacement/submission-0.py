class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Step 1: Initialize a frequency map to count characters in our window
        count = {}
        max_length = 0
        
        # 'l' is the left boundary of our sliding window
        l = 0
        max_freq = 0 # Tracks the count of the most frequent character in the current window

        # Step 2: Expand the window by moving the right pointer 'r'
        for r in range(len(s)):
            # Update the frequency count for the incoming character
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Update the maximum frequency seen in the current window scope
            max_freq = max(max_freq, count[s[r]])
            
            # Calculate current window size: (r - l + 1)
            # Step 3: Check if the number of characters we need to replace exceeds 'k'
            while (r - l + 1) - max_freq > k:
                # The window is invalid! Shrink it from the left
                count[s[l]] -= 1
                l += 1
                
            # Step 4: Update our global maximum length record
            max_length = max(max_length, r - l + 1)
            
        return max_length