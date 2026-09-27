class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkedMap = {} #maps value : index

        for i, num in enumerate(nums):
            if num in checkedMap:
                return True
            else:
                checkedMap[num] = i
        return False