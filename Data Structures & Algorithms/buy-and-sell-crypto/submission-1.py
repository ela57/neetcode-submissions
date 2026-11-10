class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 , 1
        maxprice = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            maxprice = max(maxprice, prices[r] - prices[l])
            r += 1

        return maxprice