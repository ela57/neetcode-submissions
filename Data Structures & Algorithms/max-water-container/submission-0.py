class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1
        maxof = 0

        while l < r:
            maxh = min(heights[l], heights[r])
            maxof = max(maxof, maxh * (r - l))
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1

        return maxof
            
