class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        res = 0
        for i, h in enumerate(heights):
            if h != expected[i]:
                res += 1
        return res