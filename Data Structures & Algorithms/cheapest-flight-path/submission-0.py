from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Track the cheapest price to reach each airport
        prices = [float("inf")] * n
        prices[src] = 0

        # At most k stops means we can take at most k + 1 flights
        for _ in range(k + 1):
            # Copy prices so updates in this round don't chain into extra flights
            tmp_prices = prices.copy()

            for u, v, p in flights:
                # If airport u hasn't been reached yet, we can't fly out of it
                if prices[u] == float("inf"):
                    continue

                # If flying u -> v gives a cheaper price to reach v, record it
                if prices[u] + p < tmp_prices[v]:
                    tmp_prices[v] = prices[u] + p

            # Commit the updated prices for this flight layer
            prices = tmp_prices

        return prices[dst] if prices[dst] != float("inf") else -1