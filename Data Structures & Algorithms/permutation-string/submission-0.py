class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: If s1 is longer than s2, it's impossible for s2 to contain its permutation
        if len(s1) > len(s2):
            return False

        # Step 1: Initialize frequency arrays for s1 and the sliding window in s2
        # Index 0 represents 'a', index 1 represents 'b', ..., index 25 represents 'z'
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Step 2: Populate the frequency arrays for the first 'len(s1)' characters
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Track how many character frequencies match exactly between s1Count and s2Count
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Step 3: Slide the fixed-size window across s2
        l = 0
        for r in range(len(s1), len(s2)):
            # If all 26 character frequencies match, we found a permutation!
            if matches == 26:
                return True

            # Process the incoming character on the right ('r')
            r_idx = ord(s2[r]) - ord('a')
            s2Count[r_idx] += 1
            if s1Count[r_idx] == s2Count[r_idx]:
                matches += 1
            elif s1Count[r_idx] + 1 == s2Count[r_idx]:
                # If it was equal before we incremented it, a match is now broken
                matches -= 1

            # Process the outgoing character on the left ('l')
            l_idx = ord(s2[l]) - ord('a')
            s2Count[l_idx] -= 1
            if s1Count[l_idx] == s2Count[l_idx]:
                matches += 1
            elif s1Count[l_idx] - 1 == s2Count[l_idx]:
                # If it was equal before we decremented it, a match is now broken
                matches -= 1
                
            l += 1 # Slide the window forward

        # Check one last time for the final window position
        return matches == 26