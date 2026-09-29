class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        low = prices[0]
        for price in prices:
            high = max(high, price - low)
            low = min(low, price)

        return high