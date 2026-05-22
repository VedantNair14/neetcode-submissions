class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Step 1: Initialize variables
        # We start by assuming our minimum buy price is the very first day's price
        min_buy_price = prices[0]
        max_profit = 0

        # Step 2: Iterate through the prices starting from the second day
        for i in range(1, len(prices)):
            current_price = prices[i]

            # Condition A: If the current price is CHEAPER than our minimum buy price,
            # we update our minimum buy price. We found a better day to buy!
            if current_price < min_buy_price:
                min_buy_price = current_price
            
            # Condition B: Otherwise, if selling today makes a higher profit 
            # than what we've seen before, we update our maximum profit record.
            else:
                current_profit = current_price - min_buy_price
                max_profit = max(max_profit, current_profit)

        return max_profit