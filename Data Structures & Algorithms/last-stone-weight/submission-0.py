import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Step 1: Multiply all stones by -1 to simulate a Max-Heap
        stones = [-s for s in stones]
        heapq.heapify(stones) # Transforms list into a heap in O(n) time

        # Step 2: Keep smashing stones while at least two stones remain
        while len(stones) > 1:
            # Pop the two heaviest stones (most negative numbers)
            first = heapq.heappop(stones)  # Heaviest stone (y)
            second = heapq.heappop(stones) # Second heaviest stone (x)

            # If the stones are not equal, push the remainder back
            if first != second:
                heapq.heappush(stones, first - second)

        # Step 3: Return the remaining stone's weight, or 0 if none remain
        return -stones[0] if stones else 0  