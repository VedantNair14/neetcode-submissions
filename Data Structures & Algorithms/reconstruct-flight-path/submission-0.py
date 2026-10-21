from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        
        # Sort tickets in reverse order so that pop() picks the smallest alphabetically
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []

        # Step 2: Post-order DFS (Hierholzer's Algorithm)
        def dfs(airport: str):
            # While this airport still has available flight tickets
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)
            
            # Post-order append: when all outgoing flights from here are exhausted
            res.append(airport)

        # Start itinerary from JFK
        dfs("JFK")

        # Step 3: The result is in reverse chronological order, so reverse it
        return res[::-1]  