import heapq

class MedianFinder:

    def __init__(self):
        # Two heaps:
        # small is a Max-Heap (stores smaller half, negated values for Python)
        # large is a Min-Heap (stores larger half)
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: By default, push to max-heap 'small'
        heapq.heappush(self.small, -num)

        # Step 2: Ensure every element in 'small' <= every element in 'large'
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance heap sizes (sizes should differ by at most 1)
        # We allow 'small' to hold at most 1 more element than 'large'
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If total number of elements is odd, median is the top of 'small'
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        
        # If even, median is the average of the two tops
        return (-self.small[0] + self.large[0]) / 2.0