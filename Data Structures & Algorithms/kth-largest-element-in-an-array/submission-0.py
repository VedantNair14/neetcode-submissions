import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Initialize an empty min-heap
        min_heap = []
        
        # Step 2: Iterate through every number in the array
        for num in nums:
            # Push the current number onto the heap
            heapq.heappush(min_heap, num)
            
            # If the heap grows larger than k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # Step 3: The root of the min-heap is the kth largest element
        return min_heap[0]