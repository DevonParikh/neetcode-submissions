class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {} # maps amt : [nums]
        res = []
        maxFreq = 1
        m[1] = {nums[0]}

        for num in nums[1:]:
            amt = 1
            while amt in m:
                if num in m[amt]:
                    amt += 1
                    if amt not in m:
                        m[amt] = {num}
                        maxFreq = amt
                        amt = 0
                else:
                    m[amt].add(num)
                    amt = 0
        res.extend(m[maxFreq])
        maxFreq -= 1
        while len(res) < k:
            res.extend(m[maxFreq] - m[maxFreq + 1])
            maxFreq -= 1
        return res