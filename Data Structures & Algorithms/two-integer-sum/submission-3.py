class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} # maps number to index
        for index, num in enumerate(nums):
            if target - num in m:
                return [m[target - num], index]
            m[num] = index