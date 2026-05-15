class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Using a defaultdict to store lists of anagrams
        # The key will be a tuple of character counts (a-z)
        res = defaultdict(list)

        for s in strs:
            # Create a count array for 26 lowercase English letters
            count = [0] * 26 
            
            for char in s:
                # Map character to index 0-25
                count[ord(char) - ord('a')] += 1
            
            # Convert list to tuple so it can be used as a dictionary key
            res[tuple(count)].append(s)
            
        return list(res.values())