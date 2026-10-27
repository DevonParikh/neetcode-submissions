class Solution:
    def hammingWeight(self, n: int) -> int:
        s = f"{n:b}"
        res = 0
        for char in s:
            res += int(char)
        return res