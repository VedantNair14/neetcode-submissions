import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Step 1: Compute squared distance for each point and format as [dist, x, y]
        minHeap = []
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])
            
        # Step 2: Transform the list into a min-heap in O(n) time
        heapq.heapify(minHeap)
        
        # Step 3: Extract the k smallest (closest) points from the min-heap
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            
        return res