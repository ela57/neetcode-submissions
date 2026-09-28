class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for c in range(2, len(cost) + 1):
            min1 = dp[c - 1] + cost[c - 1]
            min2 = dp[c- 2] + cost[c - 2]
            dp[c] = min(min1, min2)
        return dp[len(cost)]
