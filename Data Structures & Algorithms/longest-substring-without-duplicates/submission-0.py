class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Step 1: Initialize a set to track unique characters in our current window
        char_set = set()
        
        # 'l' is the left boundary of our sliding window
        l = 0
        max_length = 0

        # Step 2: Loop through the string with 'r' as the right boundary
        for r in range(len(s)):
            # Step 3: If we hit a duplicate character, shrink the window from the left
            # until the duplicate character is completely removed from our set
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Step 4: Add the new character to our window set
            char_set.add(s[r])
            
            # Calculate the current window size and update max_length if it's larger
            # Formula for window size: (Right Index - Left Index + 1)
            current_window_size = r - l + 1
            max_length = max(max_length, current_window_size)
            
        return max_length