class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ""
        for s in strs:
            # Format: length + delimiter + original string
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        """Decodes a single string back into a list of strings."""
        res, i = [], 0
        
        while i < len(s):
            # Find the delimiter to determine the length of the string
            j = i
            while s[j] != "#":
                j += 1
            
            # The length is the integer between index i and j
            length = int(s[i:j])
            
            # Extract exactly 'length' characters after the '#'
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer to the start of the next encoded block
            i = j + 1 + length
            
        return res