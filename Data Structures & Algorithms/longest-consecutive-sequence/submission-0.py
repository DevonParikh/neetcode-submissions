class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set()
        m = nums[0]
        res = 1
        for num in nums:
            if num < m:
                m = num
            if num not in s:
                s.add(num)
        count = 1
        while s:
            s.remove(m)
            if m+1 in s:
                count += 1
                m = m+1
                if count > res:
                    res = count
            else:
                count = 1
                if not s:
                    break
                m = min(s)

        return res