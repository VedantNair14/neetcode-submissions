class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: If the target string 't' is empty or longer than 's'
        if not t or len(s) < len(t):
            return ""

        # Step 1: Count target characters needed from 't'
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        # 'window' tracks the character counts inside our sliding window
        window = {}
        
        # 'have' tracks how many unique characters have met their target frequency requirements
        # 'need' is the total number of unique characters in 't' that must be satisfied
        have, need = 0, len(countT)
        
        # Record tracking variables: [length, left_index, right_index]
        # We initialize length to infinity so any real window will beat it
        res, resLen = [-1, -1], float("inf")
        
        # Step 2: Slide the right pointer 'r' across the string
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            
            # If the current character is part of our target list,
            # check if we have accumulated exactly the amount we need
            if char in countT and window[char] == countT[char]:
                have += 1
                
            # Step 3: While our window fulfills all requirements, try to shrink it
            while have == need:
                # Update our minimum window record if the current window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                # Pop the leftmost character out of our window to test if it's still valid
                left_char = s[l]
                window[left_char] -= 1
                
                # If removing this character breaks our checklist condition, decrement 'have'
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                    
                l += 1 # Slide the left pointer forward
                
        # Step 4: Extract the minimum substring or return empty string if no window was found
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""