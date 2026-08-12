from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Step 1: Count frequency of each task
        count = Counter(tasks)
        
        # Step 2: Push frequencies into a Max-Heap (negated values for Python)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        # Queue to store tasks waiting on cooldown: stores [remaining_count, available_time]
        q = deque()
        
        time = 0
        
        # Step 3: Process tasks until both Heap and Queue are empty
        while maxHeap or q:
            time += 1
            
            # If we have tasks ready to execute, run the most frequent one
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1  # Reduce remaining count by 1
                if cnt != 0:
                    # Task still needs to run in the future; put it on cooldown
                    q.append([cnt, time + n])
            
            # Check if the task at the front of the queue has finished cooldown
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time