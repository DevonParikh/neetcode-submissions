class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {} # mapping value : index

        for index, val in enumerate(nums):
            if (target - val) in map1:
                return [map1[target-val], index]
            else:
                map1[val] = index
