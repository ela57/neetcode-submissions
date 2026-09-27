class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        curr, prev = 1, 1
        for i in range(n - 1):
            curr, prev = curr + prev, curr
        return curr