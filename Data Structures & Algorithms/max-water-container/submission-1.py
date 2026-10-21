class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxAmt = 0
        while left < right:
            short = min(heights[left], heights[right])
            if short * (right-left) > maxAmt:
                maxAmt = short * (right-left)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxAmt