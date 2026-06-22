class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        # Step 1: Ensure A is always the shorter array.
        # This keeps our binary search runtime capped at O(log(min(m, n)))
        if len(B) < len(A):
            A, B = B, A
            
        # Initialize binary search boundaries on the shorter array A
        l, r = 0, len(A) - 1
        
        while True:
            # Pick a partition index 'i' in array A
            i = l + ((r - l) // 2)
            # Calculate the corresponding partition index 'j' in array B
            j = half - i - 2
            
            # Step 2: Handle boundaries cleanly using infinity if a partition side is empty
            Aleft  = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            
            Bleft  = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            # Step 3: Check if we found the correct partition point
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements: The median is the single smallest element of the right half
                if total % 2:
                    return min(Aright, Bright)
                # Even total elements: Average of the maximum left element and minimum right element
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                
            elif Aleft > Bright:
                # Too many elements from A's left side. Move A's partition line left.
                r = i - 1
            else:
                # Too few elements from A's left side. Move A's partition line right.
                l = i + 1