class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two-pointer approach:
        # i -> best day to buy so far (lowest price seen)
        # j -> current day we're considering selling on

        i, j = 0, 1
        maxProfit = 0

        while j < len(prices):
            # If selling on day j is profitable with buy on day i
            if prices[j] > prices[i]:
                # Update max profit if this transaction is better
                maxProfit = max(maxProfit, prices[j] - prices[i])
            else:
                # Found a cheaper buying day, move i to j
                # (you always want the lowest buy price before selling)
                i = j

            # Move to the next day
            j += 1

        # Return the best profit found (0 if no profitable trade exists)
        return maxProfit
